from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField

from .models import *


class UserPersonalForm(ModelForm):

    class Meta:
        model = UserPersonalInfo
        fields = '__all__'
        exclude = ['user']


class SummaryForm(ModelForm):
    class Meta:
        model = Summary
        fields = '__all__'
        exclude = ['user']


class EmploymentForm(ModelForm):
    class Meta:
        model = EmploymentDetail
        fields = '__all__'
        exclude = ['user']


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['user']


class SocialForm(ModelForm):
    class Meta:
        model = Social
        fields = '__all__'
        exclude = ['user']


class UserSkillForm(ModelForm):
    class Meta:
        model = UserSkill
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'skill': forms.CheckboxSelectMultiple(),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
