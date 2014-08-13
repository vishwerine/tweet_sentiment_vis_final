from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import index, emotion, charts, linechart, sample ,piechart


urlpatterns = patterns('',
    (r'^index/$',index),
    (r'^emotion/$', emotion),
    (r'^piechart/$',piechart),
    (r'^linechart/$',linechart),
    (r'^sample/$',sample),
    # Examples:
    # url(r'^$', 'tweetsentimentvis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
