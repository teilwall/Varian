from django.db import models
from django.contrib.auth.models import User
from DOCTOR.models import *
from PATIENT.models import *
import datetime
# Create your models here.

# Model For Appointment
class Appointment(models.Model):
	docterid = models.ForeignKey('DOCTOR.Docter',on_delete = models.CASCADE)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)
	machine = models.TextField(max_length=50, null=True,default="")
	organ = models.CharField(max_length=40,null=True,default="")
	time = models.CharField(max_length =40)
	date = models.CharField(max_length=40,default="")
	status = models.BooleanField(max_length = 15, default=0)
	wheelchair = models.BooleanField(default=False)


# Model For RoomReservation
class RoomReservation(models.Model):
    room_number = models.ForeignKey('Rooms', on_delete=models.CASCADE)
    date = models.CharField(max_length=40)
    patient_id = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)


# Model For Rooms
class Rooms(models.Model):
    room_number = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(default=4)
    taken_beds = models.IntegerField(default=0)
    gender = models.CharField(max_length=40, default='Female')