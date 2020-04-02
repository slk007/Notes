from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# we import this form in our views fill
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')