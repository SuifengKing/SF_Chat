from django.db import models

# Create your models here.
from datetime import datetime


class UsersProfile(models.Model):
    """用户信息表"""
    # id 自增 主键 外键关联的唯一标识
    # username 唯一性 用户除id外的唯一标识
    username = models.CharField(verbose_name='用户名', max_length=20)
    # password 用户的密码 采用has256摘要算法进行加密
    password = models.CharField(verbose_name='密码', max_length=65)
    nickname = models.CharField(verbose_name='昵称', max_length=40, default=username)
    date_joined = models.DateTimeField(verbose_name='注册时间', default=datetime.now)
    last_login = models.DateTimeField(verbose_name='上次登录时间', default=None, null=True)
    last_ip = models.CharField(verbose_name='上次登录IP', max_length=20, default=None, null=True)


class Messages(models.Model):
    """普通消息表"""
    # id 自增 主键 外键关联的唯一标识
    send_to = models.ForeignKey(UsersProfile, verbose_name='接收用户', on_delete=models.CASCADE, related_name='send_to')
    from_user = models.ForeignKey(UsersProfile, verbose_name='发送用户', on_delete=models.CASCADE, related_name='from_user')
    status = models.BooleanField(verbose_name='接收状态', default=False)
    send_time = models.DateTimeField(verbose_name='发送时间')
    content = models.TextField(verbose_name='消息内容')
    send_type = models.CharField(verbose_name='发送类型', max_length=10)


class Friends(models.Model):
    """好友表"""
    user_id = models.ForeignKey(UsersProfile, verbose_name='用户', on_delete=models.CASCADE, related_name='user_id')
    friend_id = models.ForeignKey(UsersProfile, verbose_name='好友', on_delete=models.CASCADE, related_name='friend_id')
    alias = models.CharField(verbose_name='备注昵称', max_length=40, default='')


class Groups(models.Model):
    """群组信息表"""
    # id  群ID 主键 自增 关联群组信息的唯一标识
    name = models.CharField(verbose_name='群名称', max_length=20)
    create_time = models.DateTimeField(verbose_name='创建时间')
    admin_id = models.ForeignKey(UsersProfile, verbose_name='群主ID', on_delete=models.CASCADE)


class GroupsUsers(models.Model):
    """群用户关联表"""
    user_id = models.ForeignKey(UsersProfile, on_delete=models.CASCADE, verbose_name='群成员ID')
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name='群ID')
    join_time = models.DateTimeField(verbose_name='入群时间')
    group_nick = models.CharField(verbose_name='群内昵称', max_length=40)


class GroupMsgContent(models.Model):
    """群消息内容关联表"""
    content = models.TextField(verbose_name='消息内容')
    from_id = models.ForeignKey(UsersProfile, on_delete=models.CASCADE, verbose_name='发送者ID')
    send_time = models.DateTimeField(verbose_name='发送时间')


class GroupMsgToUser(models.Model):
    """群消息用户关联表"""
    group_msg_id = models.ForeignKey(GroupMsgContent, on_delete=models.CASCADE, verbose_name='群消息ID')
    # user_id = models.CharField()
    status = models.BooleanField(verbose_name='接收状态', default=False)











