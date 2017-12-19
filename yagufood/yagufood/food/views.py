from django.shortcuts import render

# Create your views here.

def food_order(request):
	return render(request, 'food/food_order.html')