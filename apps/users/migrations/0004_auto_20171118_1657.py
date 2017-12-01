# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-18 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171117_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='moble',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='moblie',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de\u5bc6\u7801')], max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='adress',
            field=models.CharField(default='', max_length=100, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/defult.png', max_length=50, upload_to='upload/iamge/%Y/%m'),
        ),
    ]
