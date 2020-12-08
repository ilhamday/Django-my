from django.db import models
  
# Create your models here.

# Model for storing pet information | model is like a table
class Pet(models.Model):
    
    SEX_CHOICES = [('M','Male'), ('F','Female')]

    # the fields name
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    # table relationship
    # a pet can have many vaccine and the same vaccine can be applied to many pets
    # many-to-many relationship
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)