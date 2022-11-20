from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.db import models

class UserDetailsForm(forms.Form):
    id = forms.IntegerField()
    class Meta:
        field = 'id'


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields= (   
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            )
    def save(self, commit=True):
        user= super(RegistrationForm,self).save(commit=False)
        user.first_name =self.cleaned_data['first_name']
        user.last_name =self.cleaned_data['last_name']
        user.email =self.cleaned_data['email']

        if commit:
            user.save()

        return user



class EditUserProfileForm(UserChangeForm):
    
    class Meta:
        model=User
        fields= [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
            ]
        

class PasswordChangingForm(PasswordChangeForm):
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': "Introduce tu antigua contraseña"}))
    new_password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': "Introduce tu nueva contraseña"}))
    new_password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': "Vuelve a introducir tu nueva contraseña"}))



    class Meta:
        model= User
        fields = [
            'old_password',
            ' new_password1',
            ' new_password2'
        ]
