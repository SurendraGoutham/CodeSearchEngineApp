'''
Created on 21-Dec-2015

@author: 00003179
'''
from django.conf.urls import patterns, url
from webApp import views

urlpatterns = patterns('',
    url(r'^$', views.search),
)
