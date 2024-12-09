from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',cv,name='cv'),
    path('sname/',sname,name='sname')
]
