from yagujango import views
from django.conf.urls import url

urlpatterns = [
    url(r'^stadium/$', views.stadium, name='stadium'),
]