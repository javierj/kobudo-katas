from django.conf.urls import patterns, include, url
from gindex.views import gindex_for, repository_form
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoGIndexDemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # Example user/repo_name
    url(r'^gindex/(.*)/(.*)/$', 'gindex.views.gindex_for'),
    url(r'^gindex/$', 'gindex.views.repository_form'),
    url(r'^/$', include(gindex_for)),
    url(r'^$', include(gindex_for)),
)
