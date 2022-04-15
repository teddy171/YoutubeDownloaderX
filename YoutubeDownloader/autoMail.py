#发送邮件的
import smtplib
from email.mime.text import MIMEText
import os
from email.header import Header
# class Split:
#     def __init__(self, source, n) -> None:
#         # 切成多少个文件，奇数
#         self.n = n
            
#         path = os.path.dirname(__file__)
        

#         self.path = os.path.join(path, source)
#         # 源文件切分后，存到此文件夹
#         self.fragment = os.path.join(path, 'fragment/')
#         if not os.path.exists(self.fragment):
#             os.mkdir(self.fragment)
#         # 还原文件的绝对路径
#         self.source = source
#         self.restore = os.path.join(self.fragment, source)

#     def Rb(self, abs_path):
#         """二进制方式读取文件"""
#         with open(abs_path, 'rb') as f:
#             return f.read()


#     def split(self):
#         """文件切分"""
#         frb = Rb(self.source)
#         f_ls = [open(os.path.join(self.fragment, str(i)), 'wb') for i in range(N)]
#         for i in range(len(frb)):
#             if i % 2 == 0:
#                 f_ls[i % self.n].write(frb[i: i + 2])
#         for f in f_ls:
#             f.close()


#     def combine(self):
#         """合并分片，还原文件"""
#         f = open(restore, 'wb')
#         fb_ls = [rb(os.path.join(fragment, str(i))) for i in range(N)]
#         le = sum(len(frb) for frb in fb_ls)
#         for i in range(le):
#             if i % 2 == 0:
#                 f.write(fb_ls[i % N][int(((i / 2) // N) * 2): int(((i / 2) // N) * 2) + 2])
#         f.close()


#     def checkout(self):
#         """计算还原率"""
#         o = rb(source)
#         t = sum(i == j for i, j in zip(rb(restore), o))
#         print('还原率', t / len(o))


def send_email(subject, content, receiver):

    mail_host="smtp.office365.com"  #set server

    mail_user="teddy171_QQH@outlook.com"    #user name

    mail_pass="Wenqi2020@qqh"   #password

    message = MIMEText(content, 'plain', 'utf-8')

    message['From'] = Header(mail_user, 'utf-8')
    message['To'] = Header(receiver)
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP(mail_host,587)

    smtpObj.connect(mail_host, 587)

    smtpObj.ehlo() # 用户认证 

    smtpObj.starttls() # 明文通信协议的扩展，能够让明文的通信连线直接成为加密连线（使用SSL或TLS加密），而不需要使用另一个特别的端口来进行加密通信，属于机会性加密
    smtpObj.login(mail_user,mail_pass)  

    smtpObj.sendmail(mail_user, receiver, message.as_string())

    print('Mail send successfully.')