from django.contrib import admin
from .models import SchoolSelfies, surveyor_registration,SchoolMaster, HRTeachers, InfrastructureDetails, Students, MidDayMealQuality, TeachingQuality, MDMDataDetails, MDMData, TeachersDetails
# Register your models here.

admin.site.register(SchoolSelfies)
admin.site.register(surveyor_registration)
admin.site.register(SchoolMaster)
admin.site.register(HRTeachers)
admin.site.register(InfrastructureDetails)
admin.site.register(Students)
admin.site.register(MidDayMealQuality)
admin.site.register(TeachingQuality)
admin.site.register(MDMDataDetails)
admin.site.register(MDMData)
admin.site.register(TeachersDetails)
