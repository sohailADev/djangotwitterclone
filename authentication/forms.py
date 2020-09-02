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




# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=255, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)

#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if not user or not user.is_active:
#             raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
#         return self.cleaned_data

#     def login(self, request):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         return user