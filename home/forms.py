from .models import horseData
from django.forms import ModelForm


class CreateHorseForm(ModelForm):

    class Meta:
        #name = models.TextField(max_length=500, primary_key=True)
        #acquisitionDate = models.DateField()
        #totalAcquisitionAmount = models.IntegerField()
        #type = models.TextField(max_length=500)
        #place = models.TextField(max_length=500)
        #dispersmentClaim_Sale = models.IntegerField()
        #dispersmentDate = models.DateField()
            class Meta:
                model = horseData
                fields = ['__all__']
