from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class PersonalDetails(models.Model):
    applicant_id = models.IntegerField()
    full_name = models.CharField(max_length=30)
    parent_name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=12)
    category = models.CharField(max_length=15)
    mob_no = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=60)
    nationality = models.CharField(max_length=20)
