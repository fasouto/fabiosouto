# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template 
from django.views.generic.simple import redirect_to
from core.views import *
from blog.views import *
from blog.feeds import LatestEntriesFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {
    'rss': LatestEntriesFeed,
}


urlpatterns = patterns('',
    # Example:
    # (r'^fabiosouto/', include('fabiosouto.foo.urls')),

    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	('^$',redirect_to,{'url':'/blog/'}),

    (r'^admin/', include(admin.site.urls)),
  	(r'^blog/$', entries_index),
	(r'^blog/(?P<slug_post>[^/]+)/$', view_post),
	(r'^blog/category/(?P<slug_category>[^/]+)/$', category_index),
	
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),	

  	(r'^about/$', direct_to_template,{ 'template': 'about.html' }),
  	(r'^projects/$', direct_to_template,{ 'template': 'projects.html' }),
  	(r'^project/pemento_escorregadizo/$', direct_to_template,{ 'template': 'project_pemento.html' }),
  	(r'^contact/$', contact),
  	(r'^digital/$', direct_to_template,{ 'template': 'digital.html' }),


)
