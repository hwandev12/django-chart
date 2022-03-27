from django.urls import path
from .views import home, pieMarket

urlpatterns = [
    path('', home),
    path('market/', pieMarket)
]
