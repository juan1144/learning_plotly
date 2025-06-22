from django.urls import path
from apps.dashboard.views import dashboards

app_name = 'dashboard'

urlpatterns = [
    path('', dashboards.index, name='dashboard'),
    path('barchart/1', dashboards.card1, name='card1'),
]