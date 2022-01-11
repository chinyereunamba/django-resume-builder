from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import View

from django.contrib import messages

from .models import UserPersonalInfo
from .forms import *
from .decorators import *


# Create your views here.

class Home(View):
    def get(self, request):
        return render(self.request, 'index.html')


@unathenticated_user
def register(request):
    title = 'Sign Up'
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    else:
        form = CreateUserForm()

    context = {'form': form, 'title': title}
    return render(request, 'register.html', context)


@unathenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username Or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def userPage(request):
    userProfile = UserPersonalInfo.objects.get(user=request.user)
    form = UserPersonalForm(instance=userProfile)

    profile_pic = userProfile.profile_pic

    if request.method == "POST":
        form = UserPersonalForm(
            request.POST, request.FILES, instance=userProfile)
        if form.is_valid():
            form.save()

    context = {'form': form, 'profile_pic': profile_pic}

    return render(request, 'user.html', context)


def template(request):
    return render(request,  'template.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def personalInfo(request):
    user = UserPersonalInfo.objects.get(user=request.user)
    form = UserPersonalForm(instance=user)

    if request.method == "POST":
        form = UserPersonalForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'forms/personalDetail.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def summary(request):
    userProfile = UserPersonalInfo.objects.get(user=request.user)
    user = Summary.objects.get(user=userProfile)

    form = SummaryForm(instance=user)

    if request.method == 'POST':
        form = SummaryForm(request.POST, instance=user)

        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'forms/summary.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def employmentInfo(request):
    user = UserPersonalInfo.objects.get(user=request.user)

    employment = EmploymentDetail.objects.filter(user=user)

    if request.method == "POST":
        job_title = request.POST.get('job_title')
        employer = request.POST.get('employer')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        city = request.POST.get('city')
        description = request.POST.get('description')

        EmploymentDetail.objects.create(
            user=user,
            job_title=job_title,
            employer=employer,
            start_date=start_date,
            end_date=end_date,
            city=city,
            description=description,
        )

    context = {'employment': employment}

    return render(request, 'forms/employment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def update_employment(request, pk):
    user = UserPersonalInfo.objects.get(user=request.user)
    employment = EmploymentDetail.objects.get(id=pk, user=user)

    form = EmploymentForm(instance=employment)
    if request.method == "POST":
        form = EmploymentForm(request.POST, instance=employment)

        if form.is_valid():
            form.save()

        return redirect('employmentInfo')

    context = {'form': form}

    return render(request, 'forms/edit_employment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def delete_employment(request, pk):
    item = EmploymentDetail.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('employmentInfo')

    context = {'item': item}

    return render(request, 'forms/delete_employment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def educationInfo(request):
    user = UserPersonalInfo.objects.get(user=request.user)

    education = Education.objects.filter(user=user)
    if request.method == "POST":
        school = request.POST.get('school')
        study_field = request.POST.get('study_field')
        degree = request.POST.get('degree')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')

        Education.objects.create(
            user=user,
            school=school,
            degree=degree,
            study_field=study_field,
            start_date=start_date,
            end_date=end_date,
            description=description
        )

    context = {'education': education}

    return render(request, 'forms/education.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def update_education(request, pk):
    user = UserPersonalInfo.objects.get(user=request.user)
    education = Education.objects.get(id=pk, user=user)

    form = EducationForm(instance=education)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)

        if form.is_valid():
            form.save()

        return redirect('educationInfo')

    context = {'form': form}

    return render(request, 'forms/edit_education.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def delete_education(request, pk):
    item = Education.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('educationInfo')

    context = {'item': item}

    return render(request, 'forms/delete_education.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def socialInfo(request):
    user = UserPersonalInfo.objects.get(user=request.user)
    social = Social.objects.filter(user=user)
    if request.method == "POST":
        label = request.POST.get('label')
        link = request.POST.get('link')

        Social.objects.create(
            user=user,
            label=label,
            link=link
        )

    context = {'social': social}

    return render(request, 'forms/social.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def update_social(request, pk):
    user = UserPersonalInfo.objects.get(user=request.user)
    social = Social.objects.get(id=pk, user=user)

    form = SocialForm(instance=social)
    if request.method == "POST":
        form = SocialForm(request.POST, instance=social)

        if form.is_valid():
            form.save()

        return redirect('socialInfo')

    context = {'form': form}

    return render(request, 'forms/edit_social.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['users'])
def delete_social(request, pk):
    item = Social.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('socialInfo')

    context = {'item': item}

    return render(request, 'forms/delete_social.html', context)


def resume(request):
    user = UserPersonalInfo.objects.get(user=request.user)
    summary = Summary.objects.get(user=user)
    employment = EmploymentDetail.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    social = Social.objects.filter(user=user)[0:1]


    context = {
        'user': user,
        'summary': summary,
        'employment': employment,
        'education': education,
        'social': social,
    }
    return render(request, 'resume3.html', context)
