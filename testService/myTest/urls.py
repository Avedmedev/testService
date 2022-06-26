from django.urls import path
from myTest.views import *


urlpatterns = [
    path('', index, name='home'),
    path('myTest/index/', index, name='home'),
]
