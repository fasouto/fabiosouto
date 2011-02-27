# -*- coding: utf-8 -*- 
from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)


class EntryAdmin(admin.ModelAdmin):
     list_display=['title', 'pub_date', 'status']
     fieldsets = [
        (None,               {'fields': ['title','slug','body','body_markdown','categories']}),
        ('Advanced options', {'fields': ['pub_date','enable_comments','featured','status'], 'classes': ['collapse']}),]
     list_filter=['pub_date', 'status']
     search_fields = ['title']
     date_hierarchy = 'pub_date'
     prepopulated_fields = {"slug": ("title",)}

admin.site.register(Entry,EntryAdmin)

