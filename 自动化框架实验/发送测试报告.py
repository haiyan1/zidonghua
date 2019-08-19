import unittest
import HTMLTestRunner
import smtplib# smtplib负责发送邮件
from email.mime.text import MIMEText # MIMEText定义邮件正文
from email.header import Header #定义邮件标题

def send_email(test_report):

    with open(test_report, 'r', encoding='utf-8') as f:
        mail_body = f.read()                                    # 打开测试报告，读取报告内容作为邮件内容
    sender = '353229657@qq.com'                                # 发出邮箱
    receiver = ['qiaohaiyan@whggty.com']             # 接收邮箱
    mail_server = 'smtp.qq.com'                                # 邮箱服务地址，这里以139邮箱为例
    subject = '自动化测试报告'                             # 邮件标题
    username = '353229657'                                      # 邮箱登录名
    passwd = 'xyifsqajcjvacaca'                                         # 密码
    message = MIMEText(mail_body, 'html', 'utf-8')              # 设置邮件格式
    message['Subject'] = Header(subject, charset='utf-8')
    message['from'] = sender
    message['To'] = ','.join(receiver)
    # 邮箱登录
    smtp = smtplib.SMTP()# 实例化smtplib.SMTP()类对象
    smtp.connect(mail_server)# 连接邮件服务器
    smtp.login(username, passwd)# 登录
    # 发送邮件
    for i in receiver:
        smtp.sendmail(sender, i, message.as_string())
    smtp.quit()

# send_email("E:/python/report/测试报告_2019-08-16-15-18-18_result.html")


