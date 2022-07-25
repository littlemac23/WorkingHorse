from .models import Horse
from .models import Race
from .models import Expense
from django.forms import ModelForm
from django import forms


class CreateHorseForm(ModelForm):

        class Meta:
            model = Horse
            fields = '__all__'



class CreateRaceForm(ModelForm):

        class Meta:
            model = Race
            fields = '__all__'


class CreateExpenseForm(ModelForm):

        class Meta:
            model = Expense
            fields = '__all__'
