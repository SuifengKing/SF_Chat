# -*- coding: utf-8 -*-
# @File    : servers.py
# @Software: PyCharm

import socket
import threading
import time
import json
import MySQLdb
import hashlib


class SFChatServers(object):
    def __init__(self):
        # 创建TCP套接字
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定本地信息
        self.socket.bind(('192.168.72.1', 8888))
        # 将套接字由主动变为被动
        self.socket.listen(128)

        self.online_users = {}      # 用字典信息存储当前在线的用户
        self.users_addr = {}        # 保存用户IP

        self.db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            password='suifengking',
            db='sf_chat',
            charset='utf8'
        )

    def __del__(self):
        """服务端程序退出时关闭所有已连接的用户并关闭监听socket"""
        # 关闭套接字
        for username in self.online_users:
            self.online_users[username].close()
        self.socket.close()
        self.db.close()
        print('已结束!!!')

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
            print(recv_data)        # 调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印调试打印
            if recv_data['send_type'] == 'login':
                # 登录处理, 验证成功继续等待, 直到客户端退出, 断开连接
                if not self.login_auth(temp_socket, recv_data, client_addr=client_addr):
                    break
            elif recv_data['send_type'] == 'register':  # v1.1版本新添加了用户注册功能
                self.register(temp_socket, recv_data)
            elif recv_data['send_type'] == 'msg':
                self.send_msg(temp_socket, recv_data, send_to=recv_data['send_to'])     # 普通消息处理,转发至目标用户
            elif recv_data['send_type'] == 'online_users':
                self.send_users_list(temp_socket)       # 请求在线人数处理,
            elif recv_data['send_type'] == 'logout':
                logout_user = recv_data.get('from_user', '')
                del self.online_users[logout_user]
                self.send_msg(temp_socket, recv_data)
                print(logout_user + '已退出')
                break
            elif recv_data['send_type'] == 'recv_return':
                pass

    def login_auth(self, temp_socket, recv_data, client_addr):
        """用户登录身份验证的具体实现"""
        username = recv_data['username']
        password = recv_data['password']
        send_time = recv_data['send_time']
        sh = hashlib.sha256()
        sh.update((username + password + 'cyj').encode('utf8'))
        password_hash = sh.hexdigest()
        cur = self.db.cursor()
        cur.execute('select * from database_usersprofile where username=%s and password=%s', [username, password_hash])
        user = cur.fetchone()
        if user is not None:
            self.send_msg(temp_socket, {'result': 'ok', 'send_type': 'login'}, recv_data['send_to'])
            self.online_users[recv_data['username']] = temp_socket
            cur.execute("""update database_usersprofile set last_login=%s,last_ip=%s where username=%s""", [send_time, client_addr, username])
            self.db.commit()
            cur.close()
            return True
        else:
            self.send_msg(temp_socket, {'result': '用户不存在或密码错误!!!', 'send_type': 'login'}, recv_data['send_to'])
            cur.close()
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
            cur = self.db.cursor()
            if user_socket is None:
                # 此处用户离线存入数据库
                cur.execute("""insert into messages(send_to,from_user,status,send_time,content,send_type)
                            values(%s,%s,%s,%s,%s,%s)""",
                            [send_to, from_user, 0, send_time, msg, 'msg'])
            else:
                try:
                    user_socket.send(json.dumps(content).encode('utf-8'))
                    # 发送过去也应该存入数据库, 只是状态是已读
                    cur.execute("""insert into messages(send_to,from_user,status,send_time,content,send_type)
                                values(%s,%s,%s,%s,%s,%s)""",
                                [send_to, from_user, 1, send_time, msg, 'msg'])
                except:
                    cur.execute("""insert into messages(send_to,from_user,status,send_time,content,send_type)
                                values(%s,%s,%s,%s,%s,%s)""",
                                [send_to, from_user, 0, send_time, msg, 'msg'])
            self.db.commit()
            cur.close()

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

    def register(self, temp_socket, recv_data):
        username = recv_data['username']
        password = recv_data['password']
        send_time = recv_data['send_time']
        cur = self.db.cursor()
        cur.execute('select * from database_usersprofile where username=%s', [username])
        user = cur.fetchone()
        if user is not None:
            temp_socket.send(json.dumps({'send_type': 'register', 'result': '用户名已存在!!!', 'code': 1}).encode('utf8'))
        else:
            sh = hashlib.sha256()
            sh.update((username + password + 'cyj').encode('utf8'))
            password = sh.hexdigest()
            cur.execute('''insert into database_usersprofile(username, password, nickname, date_joined) 
            value (%s,%s,%s,%s)''', [username, password, username, send_time])
            self.db.commit()
            temp_socket.send(json.dumps({'send_type': 'register', 'result': '注册成功!!!', 'code': 0}).encode('utf8'))
        cur.close()


if __name__ == '__main__':
    server = SFChatServers()
    server.listen()






# print(socket.gethostbyname(socket.gethostname()))   #  获取局域网IP
# 获取公网IP接口
# 'http://ip.42.pl/raw'
# 'http://jsonip.com'
# 'http://httpbin.org/ip'
# 'https://api.ipify.org/?format=json'

