from django.conf.urls import url, include
#from django.contrib import admin
from mysite import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^categorys/(?P<category_id>[0-9]+)/$', views.show_category, name='categorys')
]