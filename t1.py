#!/usr/bin/env python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
_user = "test91160@163.com"
_pwd  = "pang147369"
_to   = "kakapang@foxmail.com;test91160@163.com"
# _to   = "501257367@163.com"

msg = MIMEText("Test",'plain','utf-8')
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

s = smtplib.SMTP("smtp.163.com")
s.login(_user, _pwd)
s.sendmail(_user, _to, msg.as_string())
s.quit()
print "Success!"
