from .models import horseData
from django.forms import ModelForm


class CreateHorseForm(ModelForm):

        class Meta:
            model = horseData
            fields = ('name', 'acquisitionDate', 'totalAcquisitionAmount', 'type', 'place')
