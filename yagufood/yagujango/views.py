from django.shortcuts import render


def stadium(request):
    return render(request, 'yagujango/stadium.html')