from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('',view_appointments),
    path('new_appointment',new_appointment,name='new_appointment'),
    path('update_appointment/<int:id>',update_appointment,name='update_appointment'),
    path('delete_appointment/<int:id>',delete_appointment,name='delete_appointment')

]
