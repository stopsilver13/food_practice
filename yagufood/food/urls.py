from food import views
from django.conf.urls import url

urlpatterns = [
	url(r'^intro/$', views.food_intro, name='food_intro'),
    url(r'^menu/(?P<date>[\d-]+)/(?P<stadium>[A-Za-z]+)$', views.food_menu, name='food_menu'),
]
