# _*_ coding: utf-8 _*_
import xadmin
from .models import CityDict, CourseOrg, Teacher

__author__ = 'daxiahy'
__date__ = '2017/11/22 17:06'


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'add_time']
    search_fields = ['city', 'name', 'desc', 'click_num', 'fav_num', 'image', 'address']
    list_filter = ['city', 'name', 'desc', 'click_num', 'fav_num', 'image', 'address', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'click_num', 'fav_num',
                    'add_time']
    search_fields = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'click_num', 'fav_num']
    list_filter = ['org', 'name', 'work_year', 'work_company', 'work_position', 'points', 'click_num', 'fav_num',
                   'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
