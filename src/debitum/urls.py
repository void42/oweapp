from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'debitum.views.home', name='home'),
    # url(r'^debitum/', include('debitum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ## 
    url(r'^accounts/', include('accounts.urls')),
    url(r'^tracker/', include('tracker.urls')),
)
