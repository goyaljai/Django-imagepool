from django import forms
from project.models import *


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SiteUser
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super(LoginForm,self)
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        #('2'or, 'Transgender')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())

    class Meta:
        model = SiteUser
        fields = ['username', 'gender','profile_picture', 'password']
