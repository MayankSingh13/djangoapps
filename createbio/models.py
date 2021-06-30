from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class biodata(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=60)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pincode = models.IntegerField(validators=[MaxValueValidator(999999)])
    gender = models.CharField(max_length=6)
    education = models.CharField(max_length=25)
