from .models import horseData
from django.forms import ModelForm


class CreateHorseForm(ModelForm):
    class Meta:
        model = horseData
        fields = '__all__'
