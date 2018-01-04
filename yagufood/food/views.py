from django.shortcuts import redirect, render
from food.models import Foodstore, Menu


def food_intro(request):

	if request.method == 'POST':
		print(request.POST.get('stadium'))
		return redirect('/food/menu/')

	return render(request, 'food/food_intro.html')


def food_menu(request):

	foodstores = Foodstore.objects.all()
	menus = Menu.objects.all()


	return render(request, 'food/food_menu.html', {
			'foodstores': foodstores,
			'menus': menus,
		})
