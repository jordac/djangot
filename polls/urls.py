from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	#ex /polls
	url(r'^$', views.index, name='index'),
	#ex /polls/5/
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
	#ex poll/5/results
	url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    #urls poll/5/reults
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    
)