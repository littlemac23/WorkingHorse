import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from .models import *

class RaceFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="raceDate", lookup_expr='gte', 
                           widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = DateFilter(field_name="raceDate", lookup_expr='lte', 
                         widget=forms.DateInput(attrs={'type': 'date'}))
    type = CharFilter(field_name= "type", lookup_expr='icontains')
    class Meta:
        model = Race
        fields = "__all__"
        exclude = ['month']

class ExpenseFilter(django_filters.FilterSet):

    class Meta:
        model = Expense
        fields = "__all__"
