from django import forms


class NewTweetForm(forms.Form):
    text = forms.CharField(max_length=120)