from django.db import models
# Create your models here.
class horseData(models.Model):
    """docstring fo horseData."""

    name = models.CharField(max_length=50, primary_key=True)
    acquisitionDate = models.DateField()
    totalAcquisitionAmount = models.IntegerField()
    type = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    dispersmentClaim_Sale = models.IntegerField()
    dispersmentDate = models.DateField()
