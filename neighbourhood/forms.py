from .models import Neighbourhood, Post, Profile,Business
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

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('business_name','business_logo','business_contact')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','hood']