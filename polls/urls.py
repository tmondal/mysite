from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	url(r'^$',views.home),
	url(r'^index/$',views.IndexView.as_view(), name = 'index'),
	url(r'^index/(?P<pk>\d+)/$',views.DetailView.as_view(), name = 'detail'),
	url(r'^index/(?P<pk>\d+)/results/$',views.ResultsView.as_view(), name = 'results'),
	url(r'^(?P<question_id>\d+)/vote/$',views.vote, name = 'vote'),
)
