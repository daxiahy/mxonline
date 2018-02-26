# _*_ coding: utf-8 _*_
__author__ = 'daxiahy'
__date__ = '2017/12/20 19:35'

from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_tittle = ""
    email_body = ""

    if send_type == "register":
        email_tittle = "注册激活链接"
        email_body = "请点击下面链接注册激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_tittle, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
