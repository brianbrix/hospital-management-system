from django import forms
from django.contrib.auth import authenticate
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


class PatientDetailsForm(forms.ModelForm):
    CHOICES = [('Male', 'Male'), ('Female', 'Female'),('other', 'Prefer not to say')]
    CHOICES_STATUS = [('single', 'Single'), ('Married', 'Married'),('Divorced', 'Divorced'),('Separated', 'Separated'),('other', 'Prefer not to say')]
    MEDICATIONS = [('yes', 'Yes'), ('no', 'No')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    medications = forms.ChoiceField(widget=forms.RadioSelect, choices=MEDICATIONS)
    marriage = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES_STATUS)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))
    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    medication_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    previous_conditions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'middlename', 'address', 'city', 'user_email','height', 'weight', 'contact', 'county', 'medications', 'medication_details', 'previous_conditions']

    def __init__(self, *args, **kwargs):
        super(PatientDetailsForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Firstname'})
        self.fields['middlename'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Middlename'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control', 'placeholder': 'LastName'})
        self.fields['user_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'email@example.com'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Address'})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nairobi'})
        self.fields['height'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Height(m)'})
        self.fields['weight'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Weight(kg)'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control', 'placeholder': '07xxxxxxxx'})
        self.fields['county'].widget.attrs.update({'class': 'form-control', 'placeholder': 'County'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.EmailInput(
        attrs={'placeholder': 'email@example.com', "class": "form-control"}))
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('user_password')
    #     user = authenticate(username=username, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
    #     return self.cleaned_data
    #
    # def login(self, request):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('user_password')
    #     user = authenticate(username=username, password=password)
    #     return user

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
