from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('charge/', charge, name='charge'),
    path('success/<str:args>/', success, name='success'),

]
