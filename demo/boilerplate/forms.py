from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #working with users

# This area defines what the form contains so the fields
# https://docs.djangoproject.com/en/4.0/topics/forms/
class NameForm(forms.Form):
    # subject = forms.CharField(max_length=100)
    your_name = forms.CharField(label='Your name', max_length=100,
    # widget=forms.TextInput(attrs={'placeholder': 'Search'})
    )
    surname = forms.CharField(label='surname', max_length=100,required=False)


#User creation form

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User #from auth
        fields = ['username','email','password1','password2']
