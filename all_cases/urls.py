from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . views import *

urlpatterns = [
    path('',view_cases,name='view_case'),
    path('new_case',new_case,name='new_case')
]
