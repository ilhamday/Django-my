from django.db import models
  
# Create your models here.

# Model for storing pet information | model is like a table
class Pet(models.Model):
    
    # Pilihan ganda M/F yang disempen ke db | Male/Female yang ditampilin di form
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
    # table relationship many-to-many relationship
    # a pet can have many vaccine and the same vaccine can be applied to many pets
    # 'Vaccine' inside () is refer to class Vaccine
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # override __str__ method, this methot tell Django what the string representation should be for this model
    def __str__(self):
        return self.name # Tell to use name field for it's default representation as string