from django.db import models

FOOD_CATEGORY = [('korean', 'korean'), ('chinese', 'chinese'), ('american', 'american'), ('dessert', 'dessert'), ('etc', 'etc')]
MENU_CATEGORY = [('main', 'main'), ('side', 'side'), ('drink', 'drink'), ('etc', 'etc')]

class Foodstore(models.Model):
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