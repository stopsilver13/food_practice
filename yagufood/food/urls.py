from food import views
from django.conf.urls import url

urlpatterns = [
	url(r'^intro/$', views.food_intro, name='food_intro'),
    url(r'^menu/$', views.food_menu, name='food_menu'),
]