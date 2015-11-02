from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from register import views

urlpatterns = patterns('',

	url(r'^accounts/$','register.views.home'),
	url(r'^accounts/login/$', 'register.views.login'),
	url(r'^accounts/login_view/$','register.views.login_view'),
	url(r'^accounts/login_view/logged_in/$','register.views.logged_in'),
	url(r'^accounts/login_view/invalid_login/$','register.views.invalid_login'),
	url(r'^accounts/logout/$', 'register.views.logout_view'),
	url(r'^accounts/registration/$', 'register.views.registration'),
	url(r'^accounts/registration/registration_success/$', 'register.views.registration_success'),	
)
