from django import forms

# Create your models here.
class ProjectModel(forms.Form):
    City1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Example: mumbai'}))
    City2  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Example: pune'}))




