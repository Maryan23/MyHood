from .models import Profile
from django.forms import ModelForm
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name','prof_photo','bio','phone_number','user')