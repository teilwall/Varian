from django.db import models
from django.contrib.auth.models import User
from DOCTOR.models import *
from PATIENT.models import *
# Create your models here.

# Model For Appointment
class Appointment(models.Model):
	docterid = models.ForeignKey('DOCTOR.Docter',on_delete = models.CASCADE)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)
	organ = models.CharField(max_length=40,null=True,default="")
	time = models.CharField(max_length =40)
	date = models.CharField(max_length=40,default="")
	status = models.BooleanField(max_length = 15, default=0)

# Model For RoomReservation
# class RoomReservation(models.Model):
#     room_number = models.ForeignKey(to_field='room_number')
#     duration = models.DateTimeField(default=datetime.date.today()+datetime.timedelta(days=WEEK))
#     patient_id = models.ForeignKey()
# Model For Rooms
# class Rooms(models.Model):
#     room_number = models.IntegerField(null=True, blank=True)
#     capacity = models.IntegerField(default=4)
#     taken_beds = models.IntegerField(default=0)