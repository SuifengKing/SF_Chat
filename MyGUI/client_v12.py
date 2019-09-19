# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 9:03
# @Author  : Yaojie Chang
# @File    : client.py
# @Software: PyCharm
import socket
import threading
import json
import time


class SFChatClient(object):
    def __init__(self):
        # 创建TCP套接字
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 链接服务器
        server_ip = '192.168.72.1'
        server_port = 8888
        server_addr = (server_ip, server_port)
        self.socket.connect(server_addr)

        self.username = ''
        self.is_login = False
        self.online_users_list = list()
        self.friends_list = list()

    def __del__(self):
        # 关闭套接字
        self.send_msg(content={}, send_type='logout')
        self.socket.close()
        print('已结束!!!')

    def login(self, username, password):
        """用户登录"""
        auth_recv = threading.Thread(target=self.recv_msg)
        auth_recv.start()
        print('正在登录, 请稍等……')
        self.username = username
        self.send_msg(content={'username': username, 'password': password}, send_type='login')
        time.sleep(1.5)

    def send_msg(self, content, send_to='', send_type='msg'):
        """
        :param content: <class 'dict'> The message that you what to send.
        :param send_to: <class 'str'> Who receives information.
        :param send_type:
        :return:
        """
        data = content
        data['send_type'] = send_type
        data['send_to'] = send_to
        data['from_user'] = self.username
        data['send_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 28800))
        # 发送数据
        self.socket.send(json.dumps(data).encode('utf-8'))  # 以json字符串经过utf-8编码发送

    def recv_msg(self):
        """接收各种消息并处理"""
        recv_data = self.socket.recv(1024)
        recv_dict = json.loads(recv_data.decode('utf-8'))
        send_type = recv_dict.get('send_type', '')
        if send_type == 'login':
            if recv_dict.get('result', None) == 'ok':
                self.is_login = True
                print('登陆成功!!!')
            else:
                print(recv_dict.get('result'))
                self.username = ''
        elif send_type == 'register':
            print(recv_dict.get('result'))
        elif send_type == 'msg':
            content = recv_dict.get('content', '')
            send_time = recv_dict.get('send_time', '')
            print(send_time + '\n收到来自'+recv_dict.get('from_user', '')+'的消息:' + content)
        elif send_type == 'online_users':
            self.online_users_list = recv_dict.get('result', None)
        elif send_type == 'search_users':
            pass
        elif send_type == 'friends':
            self.friends_list = recv_dict.get('result', None)
        return recv_dict

    def recv_msg_always(self):
        while True:
            self.recv_msg()

    def get_users_list(self):
        self.send_msg(content={}, send_type='online_users')

    def register(self, username, password):
        auth_recv = threading.Thread(target=self.recv_msg)
        auth_recv.start()
        self.username = username
        time.sleep(0.5)
        self.send_msg(content={'username': username, 'password': password}, send_type='register')
        print('正在验证信息, 请稍等……')

    def search_users(self, keyword=''):
        self.send_msg(content={'keyword': keyword}, send_type='search_users')

    def add_friend(self, username=''):
        self.send_msg(content={'username': username}, send_type='add_friend')

    def delete_friend(self, username=''):
        self.send_msg(content={'username': username}, send_type='del_friend')

    def get_friends_list(self):
        self.send_msg(content={}, send_type='friends')

    def create_group(self, group_id=''):
        pass

    def join_group(self, group_id=''):
        pass

    def quit_group(self, group_id=''):
        pass





