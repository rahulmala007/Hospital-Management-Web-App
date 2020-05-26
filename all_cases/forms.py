from django.db import models
from django.forms import ModelForm
from .models import case
from django.contrib.admin import widgets
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

    
class CaseForm(ModelForm):
    class Meta:
        model=case
        fields=['patient','receptionist','description','start_date','closed_date']
        widgets = {
            'start_date': DateInput(),
            'closed_date': DateInput()
            
        }