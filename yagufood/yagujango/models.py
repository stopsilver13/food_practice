from django.db import models

class Stadium(models.Model) :
    name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=20, blank=True)

    booking_url = models.CharField(max_length=200)
    basic = models.TextField(blank=True)
    subway = models.TextField(help_text='지하철 교통편 입력', blank=True)
    bus = models.TextField(help_text='버스 교통편 입력', blank=True)
    parking = models.TextField(help_text='주차편 입력', blank=True)

    def __str__(self) :
        return self.name