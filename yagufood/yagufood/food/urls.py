from food import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.food_order, name='food_order'),
]