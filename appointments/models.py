from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from all_cases.models import case
# Create your models here.

class Appointment(models.Model):
	patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appoint_patient')
	receptionist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appoint_receptionist')
	doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appoint_doctor')
	case = models.ForeignKey(case, on_delete=models.CASCADE, related_name='appoint_case')
	appointment_time = models.TimeField()

	def __str__(self):
		return self.patient.username + ' with ' + self.doctor.username

        