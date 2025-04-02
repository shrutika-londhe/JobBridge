"""
URL configuration for JobBridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from authentication.views import homePage
from authentication.views import authPage
from authentication.views import about
from authentication.views import contact
from dashboard.views import dashboard
from courses.views import courses;
from courses.views import ai_data1;
from courses.views import ai_data2;
from courses.views import cyber_cloud1;
from courses.views import cyber_cloud2;
from courses.views import development1;
from courses.views import development2;
from courses.views import devops_mobile1;
from courses.views import devops_mobile2;
from courses.views import enroll;

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',homePage),
    path('login/',authPage, name='authPage'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('dashboard/',dashboard, name='dashboard'),

    path('courses/',courses, name='courses'),   
    path('ai_data1/',ai_data1, name='ai_data1'),
    path('ai_data2/',ai_data2, name='ai_data2'),
    path('cyber_cloud1/',cyber_cloud1, name='cyber_cloud1'),
    path('cyber_cloud2/',cyber_cloud2, name='cyber_cloud2'),
    path('development1/',development1, name='development1'),
    path('development1/',development2, name='development2'),
    path('devops_mobile1/',devops_mobile1, name='devops_mobile1'),
    path('devops_mobile2/',devops_mobile2, name='devops_mobile2'),
    path('enroll',enroll, name='enroll')

]
