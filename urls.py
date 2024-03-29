from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^login/$', 'fantasyfoursquare.views.login'),
	(r'^users/(?P<user_id>\d+)/draft/$', 'fantasyfoursquare.views.draft'),
	(r'^game/$', 'fantasyfoursquare.views.game'),
    # Examples:
    # url(r'^$', 'FantasyFoursquare.views.home', name='home'),
    # url(r'^FantasyFoursquare/', include('FantasyFoursquare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
