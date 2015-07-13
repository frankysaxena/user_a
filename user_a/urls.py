from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'user_a.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'user_a.views.hello_runnable', name='hello_runnable'),
    url(r'^browser_info/?', include('browser_info.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
