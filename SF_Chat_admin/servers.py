# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 21:11
# @Author  : Yaojie Chang
# @File    : servers.py
# @Software: PyCharm
import socket
import threading
import json
import MySQLdb
import hashlib
import os
import django
import time
from datetime import datetime


# 引入django配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SF_Chat_admin.settings")
# 启动django
django.setup()

from database.models import UsersProfile, Messages, Friends
# from django.shortcuts import get_object_or_404


class SFChatServers(object):
    """
    V1.0  July 11 2019 10:10
    用一个字典来保存在线用户连接的socket，然后查找发送
    """
    def __init__(self):
        # 创建TCP套接字
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定本地信息
        self.socket.bind(('192.168.72.1', 8888))
        # 将套接字由主动变为被动
        self.socket.listen(128)

        self.online_users = {}      # 用字典信息存储当前在线的用户
        self.users_addr = {}        # 保存用户IP

    def __del__(self):
        """服务端程序退出时关闭所有已连接的用户并关闭监听socket"""
        # 关闭套接字
        for username in self.online_users:
            self.online_users[username].close()
        self.socket.close()
        print('服务结束……')

    def listen(self):
        """监听连接，每当用户登录到聊天工具时开始开启一个该用户的线程"""
        while True:
            new_socket, client_addr = self.socket.accept()
            print(client_addr)
            t1 = threading.Thread(target=self.recv_data, args=(new_socket, client_addr[0]))
            t1.start()
            print('线程启动')

    def recv_data(self, temp_socket, client_addr):
        """接收用户的各种信息并分别处理"""
        while True:
            # 接受数据,并解码,转换为字典形式暂时存储
            recv_data = temp_socket.recv(1024)
            recv_data = recv_data.decode('utf-8')
            recv_data = json.loads(recv_data)
            send_type = recv_data['send_type']
            print(recv_data)        # 调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印
            if send_type == 'login':
                # 登录处理, 验证成功继续等待, 直到客户端退出, 断开连接
                if not self.login_auth(temp_socket, recv_data, client_addr=client_addr):
                    break
            elif send_type == 'register':  # v1.1版本新添加了用户注册功能
                self.register(temp_socket, recv_data)
            elif send_type == 'msg':
                self.send_msg(temp_socket, recv_data, send_to=recv_data['send_to'])     # 普通消息处理,转发至目标用户
            elif send_type == 'online_users':
                self.send_users_list(temp_socket)       # 请求在线人数处理,
            elif send_type == 'friends':
                self.send_friends_list(temp_socket=temp_socket, username=recv_data.get('from_user', ''))
            elif send_type == 'search_users':
                self.search_users(temp_socket=temp_socket, keyword=recv_data.get('keyword', ''))
            elif send_type == 'add_friend':
                self.add_friend(recv_data=recv_data)
            elif send_type == 'logout':
                logout_user = recv_data.get('from_user', '')
                self.online_users[logout_user] = None
                self.send_msg(temp_socket, recv_data)
                print(logout_user + '已退出')
                break
            elif send_type == 'recv_return':
                pass

    def login_auth(self, temp_socket, recv_data, client_addr):
        """用户登录身份验证的具体实现"""
        username = recv_data['username']
        password = recv_data['password']
        sh = hashlib.sha256()
        sh.update((username + password + 'cyj').encode('utf8'))
        password_hash = sh.hexdigest()
        try:
            user = UsersProfile.objects.get(username=username, password=password_hash)
            self.send_msg(temp_socket, {'result': 'ok', 'send_type': 'login'}, recv_data['send_to'])
            self.online_users[recv_data['username']] = temp_socket
            user.last_login = datetime.now()
            user.last_ip = client_addr
            user.save()
            return True
        except:
            self.send_msg(temp_socket, {'result': '登陆失败!!!可能是用户不存在或密码错误!!!', 'send_type': 'login'}, recv_data['send_to'])
            return False

    def send_msg(self, temp_socket, content, send_to=''):
        """
        向客户端发送消息, 或者存入数据库
        :param temp_socket:
        :param content:
        :param send_to:
        :return:
        """
        # 消息反馈, 对接收到的客户端大多数行为进行反馈, 比如登录注册
        if content.get('send_type', '') == 'msg':
            temp_socket.send(json.dumps({'send_type': 'recv_return', 'result': 'ok'}).encode('utf-8'))   #
        else:
            temp_socket.send(json.dumps(content).encode('utf-8'))       #

        if content.get('send_type', '') == 'msg':
            # 此处从数据库查找目的用户，在线尝试发送，离线保存数据库
            user_socket = self.online_users.get(send_to, None)
            from_user = content.get('from_user', '')
            send_time = content.get('send_time', '')
            msg = content.get('content', '')
            # cur = self.db.cursor()
            if user_socket is None:
                # 此处用户离线存入数据库
                self.save_to_database(send_to=send_to, from_user=from_user, status=False,
                                      send_time=datetime.now(), content=msg, send_type='msg')
            else:
                try:
                    user_socket.send(json.dumps(content).encode('utf-8'))
                    # 发送过去也应该存入数据库, 只是状态是已读
                    self.save_to_database(send_to=send_to, from_user=from_user, status=True,
                                          send_time=datetime.now(), content=msg, send_type='msg')
                except:
                    self.save_to_database(send_to=send_to, from_user=from_user, status=False,
                                          send_time=datetime.now(), content=msg, send_type='msg')

    def save_to_database(self, send_to, from_user, status, send_time, content, send_type):
        """把消息数据存入数据库"""
        # 数据应该包括发送人, 发送时间, 内容, 消息状态, 接收人
        # 可以考虑使用MySQL的外键
        message = Messages()
        send_to_key = UsersProfile.objects.get(username=send_to)
        message.send_to = send_to_key
        from_user_key = UsersProfile.objects.get(username=from_user)
        message.from_user = from_user_key
        message.status = status
        message.send_time = send_time
        message.content = content
        message.send_type = send_type
        message.save()

    def send_users_list(self, temp_socket):
        """获取在线用户并发送"""
        users_list = list()
        logout_list = list()
        for user in self.online_users:
            try:
                self.online_users[user].send(json.dumps({'send_type': 'is_online'}).encode('utf-8'))
                users_list.append(user)
            except:
                logout_list.append(user)
                print(user, '已退出')
        for i in logout_list:
            if self.online_users.get(i, None) is not None:
                del self.online_users[i]
        temp_socket.send(json.dumps({'send_type': 'online_users', 'result': users_list}).encode('utf-8'))

    def register(self, temp_socket, recv_data):
        username = recv_data['username']
        password = recv_data['password']
        user_filter = UsersProfile.objects.filter(username=username)
        if user_filter:
            temp_socket.send(json.dumps({'send_type': 'register', 'result': '用户名已存在!!!', 'code': 1}).encode('utf8'))
        else:
            sh = hashlib.sha256()
            sh.update((username + password + 'cyj').encode('utf8'))
            password = sh.hexdigest()
            user_profile = UsersProfile()
            user_profile.username = username
            user_profile.password = password
            user_profile.nickname = username
            user_profile.date_joined = datetime.now()
            user_profile.save()
            temp_socket.send(json.dumps({'send_type': 'register', 'result': '注册成功!!!', 'code': 0}).encode('utf8'))

    def send_friends_list(self, temp_socket, username):
        friends_filter = Friends.objects.filter(user_id__username=username)
        friends_list = list()
        for friend in friends_filter:
            friends_list.append(friend.friend_id.username)
        temp_socket.send(json.dumps({'send_type': 'friends', 'result': friends_list}).encode('utf-8'))

    def search_users(self, temp_socket, keyword):
        user_filter = UsersProfile.objects.filter(username=keyword)
        users_list = list()
        for user in user_filter:
            users_list.append(user.username)
        temp_socket.send(json.dumps({'send_type': 'search_users', 'result': users_list}).encode('utf-8'))
    
    def add_friend(self, recv_data):
        username = recv_data.get('from_user', '')
        friend = recv_data.get('username', '')
        friend_obj = Friends()
        friend_obj.user_id = UsersProfile.objects.get(username=username)
        friend_obj.friend_id = UsersProfile.objects.get(username=friend)
        friend_obj.save()

    def del_friend(self, recv_data):
        pass


if __name__ == '__main__':
    server = SFChatServers()
    print('服务启动……')
    server.listen()


