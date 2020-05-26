from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . views import *

urlpatterns = [
    path('', profile,name='profile'),
    path('new_patient',new_patient,name='new_patient'),
    path("register", register, name="register"),
    path("hr_view", hr_view, name="hr_view"),
    path("hrpatient_view", hrpatient_view, name="hrpatient_view"),
    path("hraccounting_view", hraccounnting_view, name="hraccounting_view"),
    path("delete_patient/<int:id>", delete_patient, name="delete_patient"),
    path("delete_doctor/<int:id>", delete_doctor, name="delete_doctor"),
    path("update_patient/<int:id>", update_patient, name="update_patient"),
    path("update_doctor/<int:id>", update_doctor, name="update_doctor")

]