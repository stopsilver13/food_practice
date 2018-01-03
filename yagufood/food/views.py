from django.shortcuts import render
from food.models import Foodstore, Menu


def food_order(request):

	menus = Menu.objects.all()


	return render(request, 'food/food_order.html', {
			'menus': menus,
		})