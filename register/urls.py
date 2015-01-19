from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from register import views

urlpatterns = patterns('',

	url(r'^accounts/login/$',views.login),
	url(r'^accounts/login_view/$',views.login_view),
	url(r'^accounts/login_view/logged_in/$',views.logged_in),
	url(r'^accounts/login_view/invalid_login/$',views.invalid_login),
	url(r'^accounts/logout/$',views.logout_view),
)
