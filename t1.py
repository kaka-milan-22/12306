#!/usr/bin/env python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
_user = "67844223@qq.com"
_pwd  = "qfxgluruznkkcbae"
_to   = "kakapang@foxmail.com"
# _to   = "501257367@163.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e
