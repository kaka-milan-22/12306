#!/usr/bin/env python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
_user = "67844223@qq.com"
_pwd  = "qfxgluruznkkcbae"
_to   = "kakapang@foxmail.com;test91160@163.com"
# _to   = "501257367@163.com"

msg = MIMEText("Test".encode("utf-8"),'plain','utf-8')
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to


s = smtplib.SMTP_SSL("smtp.qq.com",465)
s.set_debuglevel(1)
s.ehlo()
# s.starttls()
s.login(_user, _pwd)
s.sendmail(_user, _to, msg.as_string())
s.quit()
print "Success!"
