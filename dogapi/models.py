from django.db import models

# Create your models here.

class Breed(models.Model):
       name = models.CharField(max_length=50)
       size = models.CharField(max_length=10, choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
       friendliness = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
       trainability = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
       sheddingamount = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
       exerciseneeds = models.IntegerField(choices=[(i, i) for i in range(1, 5)])

class Dog(models.Model):
       name = models.CharField(max_length=50)
       age = models.IntegerField()
       breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
       gender = models.CharField(max_length=7)
       color = models.CharField(max_length=20)
       favoritefood = models.CharField(max_length=50)
       favoritetoy = models.CharField(max_length=50)
