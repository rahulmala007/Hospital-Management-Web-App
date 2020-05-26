from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)
    on_duty=models.BooleanField(default=True)
    salary=models.IntegerField(default=40000)
    def __str__(self):
        return self.user.username

class Receptionist(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class HR(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username



