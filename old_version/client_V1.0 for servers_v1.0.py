# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 9:03
# @Author  : Yaojie Chang
# @File    : client.py
# @Software: PyCharm

import socket
import threading
import json


class SFChatClient(object):
    def __init__(self):
        # 创建TCP套接字
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 链接服务器
        # server_ip = '39.105.187.148'
        server_ip = '192.168.72.1'
        server_port = 8888
        server_addr = (server_ip, server_port)
        self.socket.connect(server_addr)

        self.username = ''

    def __del__(self):
        # 关闭套接字
        self.socket.close()
        print('已结束!!!')

    def login(self, username, password):
        response = self.send_msg(content={'username': username, 'password': password}, send_type='login')
        response = json.loads(response.decode('utf-8'))
        if response.get('result', None) == 'ok':
            self.username = username
            print('登陆成功!!!')
        else:
            print(response.get('result'))

    def send_msg(self, content, send_to='', send_type='msg'):
        """
        :param content: <class 'dict'> The message that you what to send.
        :param send_to: <class 'str'> Who receives information.
        :param send_type:
        :return:
        """
        data = content
        # if send_type == 'login':
        data['send_type'] = send_type
        data['send_to'] = send_to
        data['user'] = self.username
        # 发送数据
        self.socket.send(json.dumps(data).encode('utf-8'))  # 以json字符串经过utf-8编码发送
        response_data = self.recv_msg()
        return response_data

    def recv_msg(self):
        recv_data = self.socket.recv(1024)
        recv_dict = json.loads(recv_data.decode('utf-8'))
        if recv_dict.get('send_type', '') == 'login':
            pass
        elif recv_dict.get('send_type', '') == 'msg':
            content = json.loads(recv_data.decode('utf-8')).get('content', '')
            print('>>>' + content)
        elif recv_dict.get('send_type', '') == 'is_online':
            pass
        elif recv_dict.get('send_type', '') == 'online_users':
            pass
        return recv_data

    def get_users_list(self):
        response = self.send_msg(content={}, send_type='online_users')
        response = json.loads(response.decode('utf-8'))
        online_users_list = response.get('result', [])
        print(online_users_list)###################################################################################


if __name__ == '__main__':
    username = input('username:')
    password = input('password:')
    user = SFChatClient()
    user.login(username, password)

    def send():
        while True:
            user.send_msg({'content': input('>>>>')}, 'king')

    def recv():
        while True:
            user.recv_msg()

    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=recv)
    t1.start()
    t2.start()
    user.get_users_list()






# def recv_msg(udp_socket):
#     while True:
#         recv_data = udp_socket.recvfrom(1024)
#         print(recv_data[1], recv_data[0])
#         print('>>>', end='')
#
#
# def send_msg(udp_socket):
#     while True:
#         udp_socket.sendto((input('>>>')+'\n').encode('utf-8'), ('192.168.72.1', 8080))
#
#
# if __name__ == '__main__':
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.bind(('', 8888))
#     t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
#     t_send = threading.Thread(target=send_msg, args=(udp_socket,))
#     t_recv.start()
#     t_send.start()



