"""myWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
import test_home.views
from . import views

# path(route,views,name=None)
# route - 字符串，匹配的请求路径
# views - 指定路径所对应的试图处理函数的名称
# name - 地址的别名，在模板（template）中地址反向解析时使用

# path 转换器
'''
<转换器类型:自定义名>
path('page/<int:num>',views.xxx)
num 是views.xxx函数中的参数

转换器类型:
str - 匹配除'/'之外的非空字符串
int - 匹配0或者任何正整数,并返回一个int类型的值
slug - 匹配任意由ASCII字母或数字以及连字符和下划线组成的短标签
path - 匹配非空字段,包括路径分隔符'/'
'''
# re_path(reg,view,name=xxx)
'''
在url的匹配过程中可以使用正则表达式进行精确匹配
正则表达式为命名分组模式(?P<name>pattern);
    name 为组名
    pattern 为正则表达式
'''

urlpatterns = [
    path('admin/', admin.site.urls),
# http://127.0.0.1:8000/page/1
    path('page/1',views.page_1),
# http://127.0.0.1:8000
    path('',test_home.views.test_index_view,name='test_index_view'),
# http://127.0.0.1:8000/page/2-100
    path('page/<int:num>',views.page_n),
# http://127.0.0.1:8000/n/op/m 进行两位数以内的运算
    re_path(r'(?P<x>[0-9]{1,2})/(?P<op>\w+)/(?P<y>[0-9]{1,2})',views.cal_1),
# http://127.0.0.1:8000/n/操作符/m
    path('<int:n>/<str:op>/<int:m>',views.cal_2),
# http://127.0.0.1:8000/test_request
    path('test_request',views.test_request),
# http://127.0.0.1:8000/test_get_post
    path('test_get_post',views.test_get_post),

    path('test_html',views.test_html)

]
