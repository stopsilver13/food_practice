from django import forms
from django.contrib.admin import widgets

class DateForm(forms.Form):
	date = forms.DateField(widget=widgets.AdminDateWidget())