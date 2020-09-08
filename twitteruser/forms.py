from django import forms
from twitteruser.models import TwitterProfile

class AddUser(forms.Form):
    class Meta:
        model = TwitterProfile
        field = ["username", "password", "first_name", "last_name"]


class SignupForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)