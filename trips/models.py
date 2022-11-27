from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='cover_images/')
    summary = models.CharField(max_length=200)
    photo1 = models.ImageField(upload_to='trip_images/')
    photo2 = models.ImageField(upload_to='trip_images/')
    photo3 = models.ImageField(upload_to='trip_images/')
    photo4 = models.ImageField(upload_to='trip_images/')
    photo5 = models.ImageField(upload_to='trip_images/')
    photo6 = models.ImageField(upload_to='trip_images/')
    photo7 = models.ImageField(upload_to='trip_images/')
    photo8 = models.ImageField(upload_to='trip_images/')
    photo9 = models.ImageField(upload_to='trip_images/')

    def __str__(self):
        return self.title
