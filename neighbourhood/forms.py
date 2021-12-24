from .models import Profile
from django.forms import ModelForm
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('prof_photo','bio','name','phone_number','user')