from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput

from . models import Profile

########################################################################################################################
# ** UserRegistrationForm ** inherits from UserCreationForm and uses builtin User model
########################################################################################################################


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateTimeField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth']

########################################################################################################################
# ** UserUpdateForm ** uses builtin User model to update user details like username, email, about_me
########################################################################################################################


class UserUpdateForm(forms.ModelForm):
    about_me = forms.CharField(max_length=300)

    class Meta:
        model = User
        fields = ['username', 'email', 'about_me']


########################################################################################################################
# ** ProfileUpdateForm ** uses Profile model, we created that has OneToOne relationship ith User model
########################################################################################################################


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'cover_pic']


