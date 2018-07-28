''' 新版本定义django1_prj_app1的URL模式 '''
# from django.urls import path

# from . import views

# urlpatterns = [
#     #主页
#     path("",views.index, name = "index"),
#     #显示所有主题
#     path("topics/", views.topics, name="topics")
# ]
# app_name = "django1_prj_app1"
# # #https://www.cnblogs.com/qishi-bin/p/8214473.html

''' 老版本定义django1_prj_app1的URL模式 '''
from django.conf.urls import url

from . import views

urlpatterns = [
    #主页
    url(r'^$',views.index, name = 'index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic, name='topic'),
    #用于添加新主题的网页
    url(r'^new_topic/$',views.new_topic,name = 'new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry, name='edit_entry'),
]
#这个app_name一定要写上，不然会出现NoReverseMatch at /'blog' is not a registered namespace类似的错误
#https://www.cnblogs.com/qishi-bin/p/8214473.html
app_name = "django1_prj_app1"