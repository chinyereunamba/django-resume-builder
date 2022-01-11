from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
import PIL

# Create your models here.


class UserPersonalInfo(models.Model):
    user = models.OneToOneField(
        User, blank=False, null=False, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=40, blank=False, null=False)
    first_name = models.CharField(max_length=25, blank=False, null=False)
    other_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    email_address = models.EmailField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=14, blank=False, null=False)
    address = models.CharField(max_length=255)
    nationality = CountryField(blank_label='(Select Country)', blank=True)
    city = models.CharField(max_length= 20, default='San Francisco', blank=False)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(
        default="profile_img.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user}"


class RegisteredUser(models.Model):
    user = models.ForeignKey(
        UserPersonalInfo,  null=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.user}'


class Skill(models.Model):
    skill = models.CharField(max_length=30, null=False,
                             blank=False, unique=True)
    created = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f"{self.skill}"

class UserSkill(models.Model):
    user = models.ForeignKey(UserPersonalInfo, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return f'{self.user}\'s Skills'


class Summary(models.Model):
    user = models.OneToOneField(
        UserPersonalInfo, on_delete=models.CASCADE, null=False, blank=False)
    summary = models.TextField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f'{self.user.first_name}\'s Professional Summary'


class EmploymentDetail(models.Model):
    user = models.ForeignKey(
        UserPersonalInfo, on_delete=models.CASCADE, null=False, blank=False)
    job_title = models.CharField(
        max_length=40, blank=False, null=False, help_text='Proposed Job Title')
    employer = models.CharField(max_length=40, blank=False, null=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    city = models.CharField(max_length=30)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.employer


class Education(models.Model):
    user = models.ForeignKey(
        UserPersonalInfo, on_delete=models.CASCADE, null=False, blank=False)
    school = models.CharField(max_length=40, blank=False, null=False)
    degree = models.CharField(max_length=40, blank=False, null=False)
    study_field = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.school


class Social(models.Model):
    user = models.ForeignKey(
        UserPersonalInfo, on_delete=models.CASCADE, null=False, blank=False)
    label = models.CharField(max_length=10, blank=False)
    link = models.URLField(max_length=255, blank=False)

    def __str__(self):
        return self.label

class Language(models.Model):
    user = models.ForeignKey(UserPersonalInfo, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
