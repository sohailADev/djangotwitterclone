from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser import models




class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Write the username. . .'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'Enter the password. . .'
        }
  
    ))


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Write the username. . .'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'Enter the password. . .'
        }
  
    ))
    class Meta:
        model = models.TwitterUserModel
        fields = ['display_name']




