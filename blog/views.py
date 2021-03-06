# -*- coding: utf-8 -*- 

""""
Description: Simple blog engine written in django.
Author: Fabio Souto fsoutomoure@gmail.com
"""

from django.shortcuts import get_object_or_404, render_to_response 
from django.template import RequestContext 
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
from django.http import Http404
from django.contrib.sitemaps import Sitemap

from fabiosouto.blog.models import Entry, Category

class blog_sitemap(Sitemap):
    """Create the blog sitemap"""
    changefreq = 'weekly'
    priority = 0.8
    
    def items(self):
        return Entry.objects.filter(status=2)
        
    def lastmod(self, obj):
        return obj.pub_date

def entries_index(request): 
    """Show all entries paginated"""
    blog_entries = Entry.objects.filter(status=2).order_by('-pub_date')
    paginator = Paginator(blog_entries, 4)#4 posts/page
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)
    return render_to_response('blog/blog.html', {'entries':entries}, RequestContext(request)) 

def view_post(request, slug_post):
    """Show a selected post"""
    try:
        post = Entry.objects.filter(status=2).get(slug=slug_post)
    except Entry.DoesNotExist:
        raise Http404
    return render_to_response('blog/post.html', {'post':post, 'DISQUS_SHORTNAME':settings.DISQUS_SHORTNAME}, RequestContext(request))
    
def category_index(request, slug_category):
    """List all post from a selected category"""
    selected_category = get_object_or_404(Category, slug=slug_category)
    category_entries = selected_category.entry_set.filter(status=2).order_by('-pub_date')
    paginator = Paginator(category_entries, 4)#4 posts/page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)
    return render_to_response('blog/category_index.html', {'entries':entries, 'category':selected_category}, RequestContext(request))