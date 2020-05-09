from django import forms
from django.contrib.auth.forms import UserCreationForm

from hospital_management_system.models import *


class CustomUserCreationForm(forms.ModelForm):
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))
    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))

    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'address', 'city', 'user_email']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Firstname'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control', 'placeholder': 'LastName'})
        self.fields['user_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'email@example.com'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Address'})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nairobi'})
        # self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        # self.fields['user_email'].widget.attrs.update({'class': 'form-control'})
        # self.fields['user_email'].widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.EmailInput(
        attrs={'placeholder': 'email@example.com', "class": "form-control"}))
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))

    class Meta:
        model = Users
        fields = ("username", "user_password")


class DocLoginForm(forms.Form):
    doc_username = forms.CharField(max_length=100, widget=forms.EmailInput(
        attrs={'placeholder': 'email@example.com', "class": "form-control"}))
    doctor_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))

    class Meta:
        model = Doctors
        fields = ("doc_username", "doctor_password")
