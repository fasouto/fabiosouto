# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.sitemaps import ping_google

import datetime


class Category(models.Model):
    """Each post have 0-N categories related"""
    title = models.CharField(max_length=250, help_text="Maximum 250 characters") 
    slug = models.SlugField(unique=True, help_text="Unique name generated using the title")
    description = models.TextField() 
    
    def __unicode__(self): 
        return self.title 
        
    def get_absolute_url(self): 
        return "/categories/%s/" % self.slug 

    class Meta:
        verbose_name = "categoria"

class Entry(models.Model):
    """This is basically the model describing a blog post"""
    STATUS_CHOICES = (
        (1, ('Draft')),
        (2, ('Public')),
    )
    title = models.CharField(max_length=250, help_text="250 caracteres como máximo")
    slug = models.SlugField(unique_for_date='pub_date') 
    body = models.TextField(blank=True) 
    body_markdown = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now) 
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2) #By default the posts are published
    categories = models.ManyToManyField(Category, blank=True) 
    
    def __unicode__(self): 
        return self.title 
    
    def get_absolute_url(self): 
        return "/blog/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
        
    def save(self):
        import markdown
        if self.body_markdown != "":
            self.body = markdown.markdown(self.body_markdown)
        super(Entry, self).save()
        try:
            ping_google()
        except Exception:
            pass
        
    class Meta:
        verbose_name = "post"