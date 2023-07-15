from django.db import models
class Contact(models.Model):
    email=models.CharField(max_length=50)
    text=models.TextField()
    def __str__(self):
        return self.email

# Create your models here.
