from django.db import models

class Trip(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='cover_images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.title
