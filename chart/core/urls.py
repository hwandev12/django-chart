from django.urls import path
from .views import home, pieMarket

urlpatterns = [
    path('', home, name='home'),
    path('market/', pieMarket, name='market')
]
