from django.db import models
from django.contrib.auth.models import User
from all_cases.models import case

# Create your models here.
class bill(models.Model):
    case = models.ForeignKey(case, on_delete=models.CASCADE, related_name='case_bill')
    amount = models.IntegerField()
    quantity = models.IntegerField()
    bill_date = models.DateField()
    bill_details = models.CharField(max_length=500)
    is_paid = models.BooleanField(default=False)
    remaining_amount=models.IntegerField()


    def __str__(self):
        return self.case.patient.username