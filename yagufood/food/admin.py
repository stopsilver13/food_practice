from django.contrib import admin
from food.models import Foodstore, Menu


@admin.register(Foodstore)
class FoodstoreAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'contact']
	list_display_link = ['name', 'category', 'contact']
	list_filter = ['stadium', 'category', 'is_contain_main', 'is_contain_side', 'is_contain_drink', 'is_contain_etc']
	search_fields = ['name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ['group', 'store', 'name', 'price']
	list_display_link = ['group', 'store', 'name', 'price']
	list_filter = ['group', 'store']
	search_fields = ['name']