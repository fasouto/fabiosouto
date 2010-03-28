# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(required=False)
	sender = forms.EmailField(required=True)
	message = forms.CharField(widget=forms.Textarea())
