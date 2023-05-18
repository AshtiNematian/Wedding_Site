from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Partner(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(max_length=20)
    phone_number = PhoneNumberField(default='+989121111111', null=False, blank=False)

