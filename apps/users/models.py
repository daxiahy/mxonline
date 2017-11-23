# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nike_name = models.CharField(max_length=10, verbose_name="昵称", default="")
    birday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), default="male", max_length=6)
    adress = models.CharField(max_length=100, default=u"", verbose_name=u"地址")
    moblie = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机")
    image = models.ImageField(upload_to="iamge/%Y/%m", default=u"image/defult.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(max_length=20, verbose_name=u"类型", choices=(("register", u"注册"), ("forget", u"找回密码")))
    # 需要把datetime.now()的括号去掉才会在实例化类时获取时间，而不是程序编译时
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    tittle = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(max_length=100, upload_to="banner/%y/%m", verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

