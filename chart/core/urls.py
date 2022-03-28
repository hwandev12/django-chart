from django.urls import path
from .views import home, pieMarket, steps

urlpatterns = [
    path('', home, name='home'),
    path('market/', pieMarket, name='market'),
    path('step/', steps, name='step')
]
