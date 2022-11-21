from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    story_image = models.ImageField(upload_to='story_images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + '...'
