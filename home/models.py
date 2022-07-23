from django.db import models
# Create your models here.
class horseData(models.Model):
    """docstring fo horseData."""

    name = models.CharField(max_length=50, primary_key=True)
    acquisitionDate = models.DateField()
    totalAcquisitionAmount = models.IntegerField()
    type = models.TextField(max_length=500)
    place = models.TextField(max_length=500)
    dispersmentClaim_Sale = models.IntegerField()
    dispersmentDate = models.DateField()

class raceData(models.Model):

    total = models.IntegerField()
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    dateOfRace = models.DateField()
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    finish = models.CharField(max_length=50)

class expenseData(models.Model):
    description = models.CharField(max_length = 50)
    total = models.IntegerField()
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
