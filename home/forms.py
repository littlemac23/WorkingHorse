from .models import Horse
from .models import Race
from .models import Expense
from django.forms import ModelForm
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateHorseForm(ModelForm):

        class Meta:
            model = Horse
            fields = ["name", "acquisitionDate", "totalAcquisitionAmount", "type", "place"]
            widgets = {
                'acquisitionDate': DateInput(),
            }

class SellHorseForm(forms.ModelForm):

        class Meta:
            model = Horse
            fields = ["sold", "sellingPrice"]



class CreateRaceForm(ModelForm):

        class Meta:
            model = Race
            fields = ["earning", "raceDate", "finish", "type", "name"]
            widgets = {
                'raceDate': DateInput(),
            }


class CreateExpenseForm(ModelForm):
    category = forms.ChoiceField(
        choices=Expense.CATEGORY_CHOICES,
        label="Expense Category",
        help_text="Select the type of expense",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    description = forms.CharField(
        max_length=120,
        label="Expense Description",
        help_text="Enter a clear description of what this expense covers",
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g., Spring vaccination appointment', 
            'class': 'form-control'
        })
    )
    
    total = forms.IntegerField(
        label="Amount ($)",
        help_text="Enter the total amount paid (numbers only, no $ sign or commas)",
        min_value=1,
        max_value=1000000,
        widget=forms.NumberInput(attrs={
            'placeholder': '0', 
            'class': 'form-control',
            'step': '1'
        })
    )
    
    expenseDate = forms.DateField(
        label="Date of Expense",
        help_text="When was the expense incurred? Cannot be a future date.",
        widget=DateInput(attrs={'class': 'form-control'})
    )

    def clean_expenseDate(self):
        date = self.cleaned_data['expenseDate']
        # Check if date is in the future
        if date > datetime.now().date():
            raise forms.ValidationError("Expense date cannot be in the future.")
        return date
    
    def clean_total(self):
        total = self.cleaned_data['total']
        if total <= 0:
            raise forms.ValidationError("Expense amount must be greater than zero.")
        return total

    class Meta:
        model = Expense
        fields = ["name", "category", "description", "total", "expenseDate"]
        labels = {
            'name': 'Horse',
        }
        help_texts = {
            'name': 'Select which horse this expense is associated with',
        }
