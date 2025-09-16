from django import forms
from .models import Event, NGO

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','description','location','date','skills_required']

class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name','about']
