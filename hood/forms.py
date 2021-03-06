from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'image']


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        fields = ['name','location','population','health_number','police_number','image']



class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','description','email']

        
class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post']