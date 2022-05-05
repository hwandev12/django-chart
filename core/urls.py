from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('market/', pieMarket, name='market'),
    path('line/', line, name='line'),
    path('bubble/', bubble, name='bubble'),
    path('flow/', flow, name='flow'),
    path('diagram/', diagram, name='diagram')
]
