# _*_ coding: utf-8 _*_
from django.shortcuts import render

# Create your views here.
from organization.models import CourseOrg, CityDict
from django.views.generic.base import View


# 课程机构列表功能
class OrgView(View):
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 机构数
        org_num = all_orgs.count()
        # 城市
        all_citys = CityDict.objects.all()
        return render(request, "org-list.html", {
            "all_orgs": all_orgs,
            "all_citys": all_citys,
            "org_num": org_num
        })


