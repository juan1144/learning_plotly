from django.shortcuts import render


def index(request):
    return render(request, 'dashboards/index.html')

def card1(request):
    return render(request, 'dashboards/card1.html')
