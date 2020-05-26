from django.db import models
from django.forms import ModelForm
from .models import Appointment
from django.contrib.admin import widgets
from django import forms
class TimeInput(forms.TimeInput):
    input_type = 'time'

class AppointmentForm(ModelForm):
    class Meta:
        model=Appointment
        fields=['patient','receptionist','doctor','case','appointment_time']
        widgets = {
            'appointment_time': TimeInput()
        }