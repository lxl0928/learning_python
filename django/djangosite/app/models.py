#! /usr/bin/env python3
# coding: utf-8

from django.db import models


# Create your models here.
KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文本咨询', '文本咨询'),
    ('个人心情', '个人心情'),
    ('其他', '其他'),
)

class Moment(models.Model):
    """ django.db.models子类Moment
        field:
            content: 消息的内容
            user_name: 发布人的用户名
            kind: 消息的类型
    """
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20, default="匿名")
    # 修改king定义，加入choices参数
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[5])

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    n_visits = models.IntegerField()

    def __str__(self):
        return self.headline

# 一对一关系
class Account(models.Model):
    user_name = models.CharField(max_length=80)
    password = models.CharField(max_length=255)
    reg_date = models.DateField()

    def __str__(self):
        return "Account: {0}".format(self.user_name)

class Contact(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return "{0}, {1}".format(self.account.user_name, mobile)
