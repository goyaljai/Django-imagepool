from django import forms
from project.models import *


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SiteUser
        fields = ['username', 'password']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        #('2', 'Transgender')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())

    class Meta:
        model = SiteUser
        fields = ['username', 'gender','profile_picture', 'password']
