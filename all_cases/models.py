from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class case(models.Model):
	patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_patient')
	receptionist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_receptionist')
	description = models.CharField(max_length=1000, default=None)
	start_date = models.DateField()
	closed_date = models.DateField(default=None, null=True)

	def __str__(self):
		return self.patient.username + ' with' + self.description

