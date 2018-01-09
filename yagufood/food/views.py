from django.shortcuts import redirect, render
from food.models import Foodstore, Menu, DateStoreLimit, DateMenuLimit, Order, OrderedMenu
from yagujango.models import Stadium


def food_intro(request):

	year = [2018,]
	month = ['01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10, 13)]
	day = ['01', '02', '03', '04', '05', '06', '07', '08', '09'] + [x for x in range(10,32)]

	stadiums = Stadium.objects.all()

	if request.method == 'POST':
		year = '2018'
		month = request.POST.get('month')
		day = request.POST.get('day')

		date = year + '-' + month + '-' + day
		stadium = Stadium.objects.get(pk=request.POST.get('stadium'))

		return redirect('/food/menu/{}/{}'.format(date, stadium.en_name))

	return render(request, 'food/food_intro.html', {
			'month': month,
			'day': day,
			'stadiums': stadiums,
		})


def food_menu(request, date, stadium):
	user = request.user

	# if user.profile.phone :
	# 	contact = user.profile.phone

	foodstores = DateStoreLimit.objects.filter(date=date, store__stadium=Stadium.objects.get(en_name=stadium))
	menus = DateMenuLimit.objects.filter(date=date)
	raw_date = date
	date = date.split('-')
	date = date[0] + '년 ' + date[1] + '월 ' + date[2] + '일'

	if request.method =='POST':
		raw_orders = request.POST.get('ordered_menus').split(',')
		total_price = request.POST.get('total_price')
		myorder = Order.objects.create(user=user, delivery_date=raw_date, contact='-', total_price=total_price, paid_price=0, paid_point=0)
		
		for order in raw_orders:
			order = order.split('-')
			if order[1] != '0':
				menu = Menu.objects.get(name=order[0])
				amount = order[1]
				OrderedMenu.objects.create(order=myorder, menu=menu, amount=amount)

		return redirect('/food/order/{}'.format(myorder.uuid))



	return render(request, 'food/food_menu.html', {
			'foodstores': foodstores,
			'menus': menus,
			'date': date,
		})

def food_order(request, order_uuid):

	user = request.user
	order = Order.objects.get(uuid=order_uuid)

	return render(request, 'food/food_order.html', {
			'user' : user,
			'order': order,
		})




