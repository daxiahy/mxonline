# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    # models.TextField不限制字符长度
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(max_length=4, choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")))
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时常")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(max_length=100, upload_to="upload/courses/%Y/%m", verbose_name=u"课程图片")
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"上课视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"资源名称")
    download = models.FileField(max_length=100, upload_to="course/resource/%Y/%m", verbose_name=u"资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"资源信息"
        verbose_name_plural = verbose_name
