from django.db import models

# Create your models here.
class ImageEncrytion(models.Model):
    text = models.CharField(max_length = 20)
    image = models.ImageField(upload_to = 'img/%y')

    def __str__(self):
        return self.text