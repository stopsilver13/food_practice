from django.contrib import admin
from yagujango.models import Stadium

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
	list_display = ['name', 'en_name', 'booking_url']
	list_display_link = ['name', 'en_name']
	
