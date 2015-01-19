from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^polls/',include('polls.urls',namespace = "polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('register.urls')),
    url(r'^signup/',include('signup.urls', namespace = "signup")),
     url(r'^Myblog/',include('Myblog.urls', namespace = "Myblog")),
)
