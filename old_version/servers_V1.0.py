# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 9:04
# @Author  : Yaojie Chang
# @File    : servers.py
# @Software: PyCharm

import socket
import threading
import time
import json
import MySQLdb


class SFChatServers(object):
    """
    V1.0  July 11 2019 10:10
    用一个字典来保存在线用户连接的socket，然后查找发送
    """
    def __init__(self):
        # 创建TCP套接字
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定本地信息
        self.socket.bind(('', 8888))
        # 将套接字由主动变为被动
        self.socket.listen(128)

        self.online_users = {}      # 用字典信息存储当前在线的用户

    def __del__(self):
        """析构，服务端程序退出时关闭所有已连接的用户并关闭监听socket"""
        # 关闭套接字
        for username in self.online_users:
            self.online_users[username].close()
        self.socket.close()
        print('已结束!!!')

    def listen(self):
        """监听连接，每当用户登录到聊天工具时开始开启一个该用户的线程"""
        while True:
            new_socket, client_addr = self.socket.accept()
            print(client_addr)
            t1 = threading.Thread(target=self.recv_data, args=(new_socket,))
            t1.start()
            print('线程启动')

    def recv_data(self, temp_socket):
        """接收用户的各种信息并分别处理"""
        while True:
            # 接受数据,并解码,转换为字典形式暂时存储
            recv_data = temp_socket.recv(1024)
            recv_data = recv_data.decode('utf-8')
            recv_data = json.loads(recv_data)
            print(recv_data)        # 调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印
            if recv_data['send_type'] == 'login':
                # 登录处理, 验证成功就继续进入等待消息状态, 验证失败就打破循环, 结束线程
                if self.login_auth(recv_data, temp_socket):
                    pass
                else:
                    break
            elif recv_data['send_type'] == 'msg':
                self.send_msg(temp_socket, recv_data, send_to=recv_data['send_to'])     # 普通消息处理,转发至目标用户
            elif recv_data['send_type'] == 'online_users':
                self.send_users_list(temp_socket)       # 请求在线人数处理,
            elif recv_data['send_type'] == 'recv_return':
                pass

    def login_auth(self, recv_data, temp_socket):
        #
        # 此处查询数据库并对比信息
        #
        if (recv_data['username'] == 'suifeng' and recv_data['password'] == 'suifeng') or\
                (recv_data['username'] == 'king' and recv_data['password'] == 'king'):
            self.send_msg(temp_socket, {'result': 'ok', 'send_type': 'login'}, recv_data['send_to'])
            self.online_users[recv_data['username']] = temp_socket
            return True
        else:
            self.send_msg(temp_socket, {'result': '用户不存在或密码错误!!!', 'send_type': 'login'}, recv_data['send_to'])
            return False

    def send_msg(self, temp_socket, content, send_to=''):
        """
        向客户端发送消息, 或者存入数据库
        :param temp_socket:
        :param content:
        :param send_to:
        :return:
        """
        # 消息反馈, 对接收到的客户端大多数行为进行反馈
        if content.get('send_type', '') == 'msg':
            temp_socket.send(json.dumps({'send_type': 'recv_return', 'result': 'ok'}).encode('utf-8'))   # 发送两遍是为了防止客户端接收消息阻塞
            # time.sleep(0.1)
            # temp_socket.send(json.dumps({'send_type': 'recv_return', 'result': 'ok'}).encode('utf-8'))   # 以后可能会有更好的解决方法
        else:
            temp_socket.send(json.dumps(content).encode('utf-8'))       # 发送两遍是为了防止客户端接收消息阻塞
            # time.sleep(1)
            # temp_socket.send(json.dumps(content).encode('utf-8'))       # 以后可能会有更好的解决方法

        #
        # 此处从数据库查找目的用户，在线尝试发送，离线保存数据库
        #
        if send_to == '':
            pass
        else:
            user_socket = self.online_users.get(send_to, None)
            if user_socket is None:
                pass    # 此处存入数据库
            else:
                user_socket.send(json.dumps(content).encode('utf-8'))
                pass    # 发送过去也应该存入数据库, 只是状态是已读

    def save_to_database(self):
        """把数据存入数据库"""
        # 数据应该包括发送人, 发送时间, 内容, 消息状态, 接收人
        # 可以考虑使用MySQL的外键
        pass

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


if __name__ == '__main__':
    server = SFChatServers()
    server.listen()






# print(socket.gethostbyname(socket.gethostname()))   #  获取局域网IP
# 获取公网IP接口
# 'http://ip.42.pl/raw'
# 'http://jsonip.com'
# 'http://httpbin.org/ip'
# 'https://api.ipify.org/?format=json'

