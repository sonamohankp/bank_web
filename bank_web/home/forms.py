from .models import *
from django import forms
class memberForm(forms.MultipleChoiceField):
     MODEL_CATEGORIES = (
        ('debit card', 'debit card'),
        ('credit card', 'credit card'),
        ('cheque', 'cheque'),
    )
     model_categories=forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=MODEL_CATEGORIES
    )
class dateinput(forms.DateInput):
    input_type='date'

class ResgiterFrom(forms.ModelForm):
    class Meta:
        model=delts
        fields='__all__'
        
        widgets={
            'dob':dateinput()
        }
    
        
