from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

handler404='mysite.polls.views.custom_404'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': '/Users/James/Programming/Django/pyladies/training/mysite/static/'}),
)