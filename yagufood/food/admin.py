from django.contrib import admin
from food.models import Foodstore, Menu


@admin.register(Foodstore)
class FoodstoreAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'contact']
	list_display_link = ['name', 'category', 'contact']
	list_filter = ['category']
	search_fields = ['name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ['group', 'store', 'name', 'price']
	list_display_link = ['group', 'store', 'name', 'price']
	list_filter = ['group', 'store']
	search_fields = ['name']