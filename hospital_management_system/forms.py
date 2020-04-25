from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'email@example.com', "class": "form-control"}))
    user_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'password', "class": "form-control"}))
