from django.conf.urls import patterns, url
from sms import views

urlpatterns = patterns('',

	url(r'^templates/$',views.productHome),
	url(r'^templates/sms/productupdate/$',views.productUpdate),
	url(r'^templates/sms/productdetails/$',views.productDetails),
	url(r'^templates/sms/productquiery/$',views.productQuiery),
)