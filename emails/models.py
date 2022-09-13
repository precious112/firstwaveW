from django.db import models

# Create your models here.

class Email(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=40)
    phone_number=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
