from .models import horseData
from .models import raceData
from .models import expenseData
from django.forms import ModelForm
from django import forms


class CreateHorseForm(ModelForm):

        class Meta:
            model = horseData
            fields = ('name', 'acquisitionDate', 'totalAcquisitionAmount', 'type', 'place')


class CreateRaceForm(ModelForm):

        class Meta:
            model = raceData
            fields = '__all__'


class CreateExpenseForm(ModelForm):

        class Meta:
            model = expenseData
            fields = '__all__'
