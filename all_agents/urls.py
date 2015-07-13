from django.conf.urls import patterns, url
from all_agents import views

urlpatterns = patterns('',
	url(r'^$', views.my_view, name='my_view'),
)


