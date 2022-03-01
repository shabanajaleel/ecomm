from django.db import models
from EcomAdmin.models import Product


# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    subject=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name


