from django.conf import settings
from django.db import models
from yagujango.models import Stadium

FOOD_CATEGORY = [('korean', 'korean'), ('chinese', 'chinese'), ('american', 'american'), ('dessert', 'dessert'), ('etc', 'etc')]
MENU_CATEGORY = [('main', 'main'), ('side', 'side'), ('drink', 'drink'), ('etc', 'etc')]

class Foodstore(models.Model):
    stadium = models.ForeignKey(Stadium, blank=True) # 추가
    name = models.CharField(max_length=100)
    category = models.CharField(choices=FOOD_CATEGORY, default='none', max_length=50)
    address = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to="admin/foodstore", blank=True)

    is_contain_main = models.BooleanField(default=False)
    is_contain_side = models.BooleanField(default=False)
    is_contain_drink = models.BooleanField(default=False)
    is_contain_etc = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Menu(models.Model):
    store = models.ForeignKey(Foodstore)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    group = models.CharField(choices=MENU_CATEGORY, default='main', max_length=50)
    photo = models.ImageField(upload_to="admin/menu", blank=True)

    def __str__(self):
        return self.name


class DateStoreLimit(models.Model):
	date = models.DateField()
	store = models.ForeignKey(Foodstore)

	def __str__(self):
		date_store = str(self.date) + "-" + str(self.store)
		return date_store

class DateMenuLimit(models.Model):
	date = models.DateField()
	store = models.ForeignKey(DateStoreLimit)
	menu = models.ForeignKey(Menu)
	remain_amount = models.PositiveIntegerField(default=0)

	def __str__(self):
		date_menu = str(self.date) + "-" + str(self.menu)

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	delivery_date = models.DateField()
	contact = models.CharField(max_length=20)
	total_price = models.PositiveIntegerField()
	paid_point = models.PositiveIntegerField()
	paid_price = models.PositiveIntegerField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		date_user = str(self.delivery_date) + "-" + str(self.user)
		return date_user

class OrderedMenu(models.Model):
	order = models.ForeignKey(Order)
	menu = models.ForeignKey(Menu)
	amount = models.PositiveIntegerField()

	def __str__(self):
		order_menu = str(self.order) + "-" + str(self.menu)
		return order_menu




