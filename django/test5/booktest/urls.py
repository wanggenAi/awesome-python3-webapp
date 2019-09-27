from django.conf.urls import include, url
from booktest import views
urlpatterns = [
    url(r'^static_test$', views.static_test),
    url(r'^index$', views.index),
    url(r'^show_upload$', views.show_upload),
    url(r'^upload_handle$', views.upload_handle),
    url(r'^show_areas(\d*)$', views.show_areas),
    url(r'^areas$', views.areas),
    url(r'^prov$', views.prov),
    url(r'^city(\d*)$', views.city),
    url(r'^dis$', views.dis),
]
