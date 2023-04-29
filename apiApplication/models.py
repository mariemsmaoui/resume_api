from django.db import models


# Create your models here.
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not str(value).startswith('216') or len(str(value)) != 10:
        raise ValidationError('Phone number must start with 55 and have 8 digits.')

class PersonalProfile(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    intro=models.CharField(max_length=200)
    phone = models.IntegerField(validators=[validate_phone_number])
    email = models.EmailField(max_length=100)
    birthdate = models.DateField()
    linkedin= models.URLField(max_length=200)

class Education(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    desciption = models.CharField(max_length=200)

class ProfessionalExperience(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    header = models.CharField(max_length=50)
    desciption = models.CharField(max_length=200)

class AcademicProjects(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    desciption = models.CharField(max_length=200)

class AssociativeLife(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    desciption = models.CharField(max_length=200)

class Skills(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    desciption = models.CharField(max_length=200)

class Certficates(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    desciption = models.CharField(max_length=200)

class Languages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)




