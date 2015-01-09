from django.conf.urls import patterns, url
from Myblog import views

urlpatterns = patterns('',

	url(r'^$',views.blogHome, name = 'blogHome'),

	)