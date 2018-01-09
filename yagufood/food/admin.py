from django.contrib import admin
from food.models import Foodstore, Menu, DateStoreLimit, DateMenuLimit, Order, OrderedMenu


@admin.register(Foodstore)
class FoodstoreAdmin(admin.ModelAdmin):
	list_display = ['stadium','name', 'category', 'contact']
	list_display_link = ['name', 'category', 'contact']
	list_filter = ['stadium', 'category', 'is_contain_main', 'is_contain_side', 'is_contain_drink', 'is_contain_etc']
	search_fields = ['name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	list_display = ['group', 'store', 'name', 'price']
	list_display_link = ['group', 'store', 'name', 'price']
	list_filter = ['group', 'store']
	search_fields = ['name']

@admin.register(DateStoreLimit)
class DateStoreLimitAdmin(admin.ModelAdmin):
	list_display = ['date', 'store']
	list_display_link = ['date', 'store']
	list_filter = ['store', 'date']

@admin.register(DateMenuLimit)
class DateMenuLimitAdmin(admin.ModelAdmin):
	list_display = ['date', 'store', 'menu', 'remain_amount']
	list_display_link = ['date', 'store', 'menu']
	list_filter = ['date', 'store']
	search_fields = ['menu']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['user', 'delivery_date', 'contact', 'total_price', 'paid_price', 'paid_point']
	list_display_link = ['user', 'delivery_date', 'contact']
	list_filter = ['delivery_date']
	search_fields = ['user']

@admin.register(OrderedMenu)
class OrderedMenuAdmin(admin.ModelAdmin):
	list_display = ['order', 'menu', 'amount']
	list_display_link = ['order', 'menu']
	search_fields = ['order', 'menu']