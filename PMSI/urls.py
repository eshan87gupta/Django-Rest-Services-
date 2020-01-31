"""PMSI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include


from PMSI import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('inspection.urls')),
    url('school', include('inspection.picsSerializer.urls')),
    url('school', include('inspection.school_master.urls')),
    url('surveyor', include('inspection.registration.urls')),
    url('hr', include('inspection.hrteacher.urls')),
    url('infra', include('inspection.infradetails.urls')),
    url('std', include('inspection.studentsdetails.urls')),
    url('teaching', include('inspection.teachingQualityDetails.urls')),
    url('middaymeal', include('inspection.middaymealdetails.urls')),
    url('agency', include('inspection.agencyDetails.urls')),
    url('mdmdata', include('inspection.mdmdata.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
