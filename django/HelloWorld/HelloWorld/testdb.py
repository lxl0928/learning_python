#! /usr/bin/env python3
# coding: utf-8

from django.http import HttpResponse
from TestModel.models import Test

# 数据库操作
def testdb(request):
    # insert 一个数据
    test1 = Test(name='timilong')
    test1.save()
    return HttpResponse("<p>"+ "更新成功</p>")
"""
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行
    list = Test.objects.all()

    # 通过filter设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.g et(id=1)

    # 限制返回的数据
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by('id')

    # 上面的方法联合使用
    Test.objects.filter(name='timilong').order_by('id')

    #输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1

    # 更新数据方法1
    test1 = Test.objects.get(id=1)
    test1.name = "Google"
    test1.save()

    # 更新数据方法2
    test2 = Test.objects.filter(id=2)
    test2.update(name="Facebook")

    # 更新所有列
    Test.objects.all().update(name="Twitter")

    # 删除id=1的列
    test3 = Test.objects.get(id=1)
    test3.delete()

    # 删除id=2的列
    test4 = Test.objects.filter(id=2)
    test4.delete()

    # 删除所有数据
    Test.objects.all().delete()
"""
