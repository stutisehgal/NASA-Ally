from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from allysocials import views

app_name = 'allysocials'
urlpatterns = [
    url(r"blogmainpage/$",views.showallysocials,name='blog_main_page'),
    url(r"aboutsocials/$",views.showabtallysocials,name='blog_about'),
    ]
