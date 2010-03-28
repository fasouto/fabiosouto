# -*- coding: utf-8 -*- 
from django.shortcuts import get_object_or_404, render_to_response 
from fabiosouto.blog.models import *
from django.template import RequestContext 
from django.contrib.comments.models import Comment
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.sites.models import Site
from django.conf import settings
from django.http import Http404


def entries_index(request): 
	blog_entries = Entry.objects.filter(status=2).order_by('-pub_date')
	paginator = Paginator(blog_entries,4)
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
	try:
		entries = paginator.page(page)
	except (EmptyPage, InvalidPage):
		entries = paginator.page(paginator.num_pages)
	return render_to_response('blog/blog.html',{'entries':entries},RequestContext(request)) 

def view_post(request,slug_post):
	try:
		post = Entry.objects.filter(status=2).get(slug=slug_post)
	except Entry.DoesNotExist:
		raise Http404
	return render_to_response('blog/post.html',{'post':post},RequestContext(request))