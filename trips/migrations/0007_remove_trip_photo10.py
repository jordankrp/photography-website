# Generated by Django 3.2.16 on 2023-05-13 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_trip_photo10'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='photo10',
        ),
    ]
