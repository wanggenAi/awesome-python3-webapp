from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^temp_var$', views.temp_var),
    url(r'^temp_tags$', views.temp_tags), # 模板标签
    url(r'^temp_filter$', views.temp_filter), # 模板标签
    url(r'^temp_inherit$', views.temp_inherit), # 模板继承
    url(r'^html_escape$', views.html_escape), # 模板继承
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^change_pwd$', views.change_pwd),
    url(r'^change_pwd_action$', views.change_pwd_action),
    url(r'^verify_code$', views.verify_code),
    url(r'^url_reverse$', views.url_reverse),
    url(r'^index12312321$', views.index, name='index'),
    url(r'^show_args/(\d+)/(\d+)$', views.show_args, name='show_args'),
    url(r'^show_qweqweqwargs/(?P<num1>\w+)/(?P<num2>\w+)$', views.show_kwargs, name='show_kwargs'),
    url(r'^test1_reverse$', views.test1_reverse),
    url(r'^test2_reverse$', views.test2_reverse),
]
