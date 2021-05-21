from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.IntegerField(
                widget=forms.NumberInput(
                attrs={
                    'required':'required',
                    'placeholder': 'Username',
                    'class': 'form-control'
                      }
                    )
                )
    first_name = forms.CharField(max_length=50,
                  widget=forms.TextInput(
                  attrs={
                        'required': 'required',
                        'placeholder': 'First name',
                        'class': 'form-control',
                        }
                    )
                )
    last_name = forms.CharField(max_length=50,
                  widget=forms.TextInput(
                  attrs={
                        'required': 'required',
                        'placeholder': 'Last name',
                        'class': 'form-control',
                        }
                    )
                )
    password1 = forms.CharField(
                 widget=forms.PasswordInput(
                 attrs={
                        'placeholder':'Password',
                        'required': 'required',
                        'class': 'form-control',
                        }
                    )
                )
    password2 = forms.CharField(
                 widget=forms.PasswordInput(
                 attrs={
                        'placeholder':'Confirm Password',
                        'required': 'required',
                        'class': 'form-control',
                        }
                    )
                )
    email = forms.EmailField(
             widget=forms.EmailInput(
             attrs={
                    'required': 'required',
                    'placeholder': 'Enter Email-id',
                    'class': 'form-control',
                    }
                )
            )

class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']
