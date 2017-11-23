# _*_ coding: utf-8 _*_
import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views

__author__ = 'daxiahy'
__date__ = '2017/11/22 11:07'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "墓学在线网"
    menu_style = "accordoin"
    

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['tittle', 'image', 'url', 'index', 'add_time']
    search_fields = ['tittle', 'image', 'url', 'index']
    list_filter = ['tittle', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
