from django.conf.urls import patterns,url
from clone import views


urlpatterns = patterns('',

	url(r'^movie/$','clone.views.movieview'),
	url(r'^people/$','clone.views.peopleview'),
	url(r'^studio/$','clone.views.studioview'),
)