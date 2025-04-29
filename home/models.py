from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from datetime import datetime    



class Horse(models.Model):
    name = models.CharField(max_length = 120)
    acquisitionDate = models.DateField()
    totalAcquisitionAmount = models.IntegerField()
    type = models.CharField(max_length = 120)
    place = models.CharField(max_length = 120)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    sold = models.BooleanField(default=False)
    sellingPrice = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

class Race(models.Model):
    earning = models.IntegerField()
    raceDate = models.DateField()
    finish = models.CharField(max_length = 120)
    type = models.CharField(max_length = 120)
    name = models.ForeignKey(Horse, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name) + ' ' + str(self.raceDate)

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('VETERINARY', 'Veterinary Care'),
        ('FEED', 'Feed & Nutrition'),
        ('TRAINING', 'Training & Lessons'),
        ('BOARDING', 'Boarding & Stabling'),
        ('EQUIPMENT', 'Equipment & Tack'),
        ('FARRIER', 'Farrier & Hoof Care'),
        ('TRANSPORT', 'Transportation'),
        ('COMPETITION', 'Competition & Race Fees'),
        ('INSURANCE', 'Insurance'),
        ('OTHER', 'Other Expenses'),
    ]
    
    expenseDate = models.DateField(default=datetime.now, blank=True)
    description = models.CharField(max_length = 120)
    total = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    name = models.ForeignKey(Horse, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name)+ ' ' + str(self.description) + ' ' + str(self.id)
