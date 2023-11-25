from django.db import models
from .util import *
import datetime

# Create your models here.

class Patient(models.Model):
    patient_id = models.TextField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    gender = models.TextChoices(Gender)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.TextField(null=True, blank=True)
    gender = models.TextChoices(Gender)

    def __str__(self):
        return self.name
    
class RoomReservation(models.Model):
    room_number = models.ForeignKey(to_field='room_number')
    duration = models.DateTimeField(default=datetime.date.today()+datetime.timedelta(days=WEEK))
    patient_id = models.ForeignKey()

class Rooms(models.Model):
    room_number = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(default=4)
    taken_beds = models.IntegerField(default=0)
