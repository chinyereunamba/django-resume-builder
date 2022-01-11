from django.contrib import admin
from .models import *

# Register your models here.


class UserPersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address')


class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title')


class EmploymentDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'employer', 'start_date', 'end_date')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'start_date', 'end_date')



admin.site.register(UserPersonalInfo, UserPersonalInfoAdmin)
admin.site.register(RegisteredUser)
admin.site.register(EmploymentDetail, EmploymentDetailAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Summary)
admin.site.register(Social)
