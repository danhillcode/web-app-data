from django import forms

# This area defines what the form contains so the fields
# https://docs.djangoproject.com/en/4.0/topics/forms/
class NameForm(forms.Form):
    # subject = forms.CharField(max_length=100)
    your_name = forms.CharField(label='Your name', max_length=100)