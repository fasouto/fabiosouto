# -*- coding: utf-8 -*- 
from django.db import models
import datetime

class Category(models.Model): 
	title = models.CharField(max_length=250, help_text="250 caracteres como maximo") 
	slug = models.SlugField(unique=True,help_text="Se genera un nombre recomendado automaticamente a partir del titulo. Este campo debe ser unico.") #Prepopulate lo que hace es coger el nombre del titulo de primeras dejando al usuario cambiar si es distinto
	description=models.TextField() 
	
	def __unicode__(self): 
		return self.title 
		
	def get_absolute_url(self): 
		return "/categories/%s/" % self.slug 

	class Meta:
		verbose_name="categoria"
	
	
class Entry(models.Model): 
	STATUS_CHOICES = (
        (1, ('Draft')),
        (2, ('Public')),
    )
	title = models.CharField(max_length=250,help_text="250 caracteres como máximo")
	slug=models.SlugField(unique_for_date='pub_date') 
	body=models.TextField() 
	tease = models.TextField(('tease'), blank=True, help_text=('Concise text suggested. Does not appear in RSS feed.'))
	pub_date=models.DateTimeField(default=datetime.datetime.now) 
	enable_comments = models.BooleanField(default=True)#permitimos comentarios?
	featured = models.BooleanField(default=False) #post seleccionado
	status = models.IntegerField(choices=STATUS_CHOICES, default=2) #por defecto publicadas
	categories = models.ManyToManyField(Category,blank=True) 
	
	def __unicode__(self): 
		return self.title 
	
	def get_absolute_url(self): 
		return "/blog/%s/%s/"%(self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
		
	class Meta:
	    verbose_name="post"


	


