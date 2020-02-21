from django import forms
from .models import Neighborhood,UserProfile,Business

class NewsForm(forms.ModelForm):
    class Meta:
        model=NewsForm
        exclude=['editor']
        widgets ={
            'tags':forms.CheckboxSelectMultiple(),
        }