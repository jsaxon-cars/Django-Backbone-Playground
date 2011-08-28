from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('polls.views',
    (r'^$', 'index'),
    (r'^json$', 'json'),
    (r'^(?P<poll_id>\d+)/$', 'detail'),
    (r'^(?P<poll_id>\d+)/results/$', 'results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
