# -*- coding: utf-8 -*- 
from django.contrib.syndication.feeds import Feed
from fabiosouto.blog.models import Entry

class LatestEntriesFeed(Feed):
	title = "fabiosouto.eu latests posts"
	link = "http://fabiosouto.eu/blog/"
	description = "Latests posts from Fabio Souto's blog"
	
	def items(self):
		return Entry.objects.order_by('-pub_date')[:5]
		
	def item_link(self,item):
		return 'http://fabiosouto.eu/blog/%s' % item.slug
		


