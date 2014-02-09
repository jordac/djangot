from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	#ex /polls
	url(r'^$', views.IndexView.as_view(), name='index'),
	#ex /polls/5/
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	#ex poll/5/results
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #urls poll/5/reults
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    
)