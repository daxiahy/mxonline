# _*_ coding: utf-8 _*_
__author__ = 'daxiahy'
__date__ = '2017/12/6 17:56'
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
