#! /usr/bin/python
# *-* coding:utf-8 *-*
import unittest
# 这里需要导入测试文件
from test_case import *
import HTMLTestRunner
import 发送测试报告
import smtplib # 导入smtplib模块
from email.mime.text import MIMEText
from email.header import Header
import datetime
import os
from unittest import defaultTestLoader

time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

cur_path = os.path.dirname(os.path.realpath(__file__)) #获取当前文件也就是主程序.py这个文件的路径
case_path = os.path.join(cur_path,"test_case")   #得到用例所在路径
discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py")
# 将测试用例加入到测试容器(套件)中
testunit = unittest.TestSuite()
# testunit.addTest(discover)
testunit.addTest(unittest.makeSuite(test_登录.Denglu))  # baidu.Baidu中的baidu为用例所在的.py文件的名称，Baidu为测试用例集的名称
# testunit.addTest(unittest.makeSuite(test_产品管理.Service))
# testunit.addTest(unittest.makeSuite(test_产品包管理.Product))
# testunit.addTest(unittest.makeSuite(test_授权管理.Store))

# 定义个报告存放路径，支持相对路径。
filename = 'E:\\python\\report\\' + u"测试报告_" + time + "_result.html"
fp = open(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况：")
# 执行测试用例
result=runner.run(testunit)
print(result)
fp.close()
发送测试报告.send_email(filename)
