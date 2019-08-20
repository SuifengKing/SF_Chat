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
        server_ip = '39.105.187.148'
        # server_ip = '192.168.72.1'
        server_port = 8888
        server_addr = (server_ip, server_port)
        self.socket.connect(server_addr)

        self.username = ''
        self.is_login = False
        self.online_users_list = list()

    def __del__(self):
        # 关闭套接字
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
        if self.is_login:
            self.menu()
        else:
            return

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

    def recv_msg(self):
        """接收各种消息并处理"""
        recv_data = self.socket.recv(1024)
        recv_dict = json.loads(recv_data.decode('utf-8'))
        if recv_dict.get('send_type', '') == 'login':
            if recv_dict.get('result', None) == 'ok':
                # self.username = username
                self.is_login = True
                print('登陆成功!!!')
                # self.get_users_list()   #
            else:
                print(recv_dict.get('result'))
                self.username = ''
                # raise Exception
                # exit(0)
        elif recv_dict.get('send_type', '') == 'register':
            print(recv_dict.get('result'))
        elif recv_dict.get('send_type', '') == 'msg':
            content = recv_dict.get('content', '')
            print('\n收到来自'+recv_dict.get('user', '')+'的消息:' + content)
        elif recv_dict.get('send_type', '') == 'is_online':
            pass
        elif recv_dict.get('send_type', '') == 'online_users':
            self.online_users_list = recv_dict.get('result', None)
            # print(self.online_users_list)       # 调试输出#调试输出#调试输出#调试输出#调试输出#调试输出#调试输出#调试#
        return recv_data

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

    def menu(self):
        if self.is_login:
            threading.Thread(target=self.recv_msg_always).start()
            self.get_users_list()
            print('正在获取在线人数, 请稍等……')
            time.sleep(1.5)
            flag = ''
            while flag != 'q':
                online_num = len(self.online_users_list)
                print('=======================================')    # 40
                print('|\t当前在线人数: '+str(online_num)+'\t|')
                for i in range(online_num):
                    print('|\t'+str(i)+').'+self.online_users_list[i])
                print('|\t'+str(online_num)+').刷新在线人数')
                # print(print('|\tq).退出'))
                print('=======================================')    # 40
                flag = int(input('请输入你的选择:'))
                if flag == online_num:
                    self.get_users_list()
                    print('正在获取在线人数, 请稍等……')
                    time.sleep(1.5)
                    continue
                elif flag == online_num+1:
                    exit(0)
                else:
                    username = self.online_users_list[flag]
                    text = input(username + '(输入q返回)<<<>>>')
                    while text != 'q':
                        self.send_msg(content={'content': text}, send_to=username)
                        text = input(username + '(输入q返回)<<<>>>')


if __name__ == '__main__':
    user = SFChatClient()
    while True:
        print('========欢迎使用随风聊天========')
        print('|\t\t1.)登录')
        print('|\t\t2.)注册')
        print('|\t\t3.)退出')
        print('================================')
        choice = input('请选择:')
        if choice == '1':
            user_name = input('username:')
            pwd = input('password:')
            user.login(user_name, pwd)
        elif choice == '2':
            user_name = input('Please enter username:')
            pwd = input('Please enter password:')
            re_pwd = input('Please enter password again:')
            if pwd == re_pwd:
                user.register(username=user_name, password=pwd)
            else:
                print('两次输入密码不同!!!')
                input('请按回车继续!')
        else:
            exit(0)




