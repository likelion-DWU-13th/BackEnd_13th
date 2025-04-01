from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home),
    path('create/', create, name='create'),
]