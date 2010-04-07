# -*- coding: utf-8 -*- 
from django import template
from django.db import models
import re

Entry = models.get_model('blog','entry')
Category = models.get_model('blog','category')

register = template.Library()


#Gets the categories from a given post
class EntryCategories(template.Node):
    def __init__(self, post_id , var_name):
        self.post_id = template.Variable(post_id)
        self.var_name = var_name


    def render(self, context):
        identificador_post = self.post_id.resolve(context)
        post=Entry.objects.get(pk=identificador_post)
        categories=post.categories.all()
        context[self.var_name] = categories
        return ''

@register.tag
def get_post_categories(parser, token):
    """
    Gets all post categories.

    Syntax:

        {% get_post_categories [post_id] as [var_name] %}

    Example:

        {% get_post_categories 5 as categories_list %}
    """
    bits = token.contents.split()
    if len(bits) != 4:
        raise template.TemplateSyntaxError, "get_post_categories tag takes exactly four arguments"
    if bits[2] != 'as':
        raise template.TemplateSyntaxError, "third argument to the get_latest tag must be 'as'"
    return EntryCategories(bits[1], bits[3])


#Get all blog categories
class BlogCategories(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        categories = Category.objects.all()
        context[self.var_name] = categories
        return ''

@register.tag
def get_blog_categories(parser, token):
    """
    Gets all blog categories.

    Syntax:

        {% get_blog_categories as [var_name] %}

    Example:

        {% get_blog_categories as category_list %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    argument = re.search(r'as (\w+)', arg)
    if not argument:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = argument.groups()[0]
    return BlogCategories(var_name)

#Get the latest published entries on the blog ordered by publication date
class BlogEntries(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        blog_entries = Entry.objects.filter(status=2).order_by('-pub_date')[:7]
        context[self.var_name] = blog_entries
        return ''

@register.tag
def get_blog_entries(parser, token):
    """
    Gets all blog posts

    Syntax:

        {% get_blog_entries as [var_name] %}

    Example:

        {% get_blog_entries as post_list %}
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    argument = re.search(r'as (\w+)', arg)
    if not argument:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = argument.groups()[0]
    return BlogEntries(var_name)