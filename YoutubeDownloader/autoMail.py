#发送邮件的
import smtplib
from email.mime.text import MIMEText
import os
from email.header import Header

def send_email(subject, content, receiver):

    mail_host="smtp.office365.com"  #set server

    mail_user="************"    #user name

    mail_pass="***********"   #password

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