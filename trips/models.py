from django.db import models

class Trip(models.Model):
    cover_image = models.ImageField(upload_to='cover_images/')
    summary = models.CharField(max_length=200)
