# Generated by Django 4.2.7 on 2023-11-25 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COMMON_APP', '0005_rooms_appointment_wheelchair_roomreservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='weight',
            field=models.IntegerField(default=55),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='wheelchair',
            field=models.CharField(max_length=15),
        ),
    ]
