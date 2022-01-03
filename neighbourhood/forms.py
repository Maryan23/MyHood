from .models import Neighbourhood, Profile
from django.forms import ModelForm
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('prof_photo','bio','phone_number','user')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'prof_photo','phone_number')

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('hood_image','hood_name','description')