from django.conf.urls import url, include
#from django.contrib import admin
from account import views
urlpatterns = [

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='reg'),
    url(r'^account/$', views.accountPage, name='reg'),
    url(r'^$', views.home, name='home'),
]