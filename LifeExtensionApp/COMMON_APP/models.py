from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from DOCTOR.models import *
from PATIENT.models import *
# Create your models here.

# Model For Receptionist
# class Receptionist(models.Model):
# 	name = models.CharField(max_length=40)
# 	phone = models.CharField(max_length=12,default="",unique=True)
# 	email = models.CharField(max_length=50,unique=True)
# 	address = models.CharField(max_length=200)
# 	username = models.OneToOneField(User,on_delete = models.CASCADE)



# Model For Appointment
class Appointment(models.Model):
	docterid = models.ForeignKey('DOCTOR.Docter',on_delete = models.CASCADE)
	patientid = models.ForeignKey('PATIENT.Patient',on_delete = models.CASCADE)
	# machine = models.CharField(max_length=40)
	time = models.CharField(max_length =40)
	date = models.CharField(max_length=40,default="")
	status = models.BooleanField(max_length = 15, default=0)


# Model For HR
# class HR(models.Model):
# 	name = models.CharField(max_length=40)
# 	phone = models.CharField(max_length=12,default="",unique=True)
# 	email = models.CharField(max_length=50,unique=True)
# 	address = models.CharField(max_length=200)
# 	username = models.OneToOneField(User,on_delete = models.CASCADE)


# class BedReservation(models.Model):
#     room_number = models.ForeignKey(to_field='room_number')
#     duration = models.DateTimeField(default=datetime.date.today()+datetime.timedelta(days=7))
#     patient_id = models.ForeignKey()


# class Rooms(models.Model):
#     room_number = models.IntegerField(null=True, blank=True)
#     capacity = models.IntegerField(default=4)
#     taken_beds = models.IntegerField(default=0)