from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),


    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('user/', userPage, name='user'),
    path('template/', template, name='template'),


    path('personalInfo/', personalInfo, name='personalInfo'),

    path('professionalSummary/', summary, name='summary'),

    path('employment/', employmentInfo, name='employmentInfo'),
    path('employment/<str:pk>/', update_employment, name='update_employment'),
    path('remove_employment/<str:pk>/',
         delete_employment, name='delete_employment'),

    path('education/', educationInfo, name='educationInfo'),
    path('education/<str:pk>/', update_education, name='update_education'),
    path('remove_education/<str:pk>/', delete_education, name='delete_education'),


    path('social/', socialInfo, name='socialInfo'),
    path('social/<str:pk>/', update_social, name='update_social'),
    path('remove_social/<str:pk>/', delete_social, name='delete_social'),

    # path('skills/', skills, name='skills'),
    # path('remove_skill/<str:pk>/', delete_skill, name='delete_skill'),

    path('resume/', resume, name="resume")
]
