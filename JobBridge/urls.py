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
from authentication.views import indexPage;
from authentication.views import logout_view;
from authentication.views import authPage;
from authentication.views import about;
from authentication.views import contact;
from dashboard.views import dashboard;
from courses.views import courses;
from courses.views import ai_data1;
from courses.views import ai_data2;
from courses.views import cyber_cloud1;
from courses.views import cyber_cloud2;
from courses.views import development1;
from courses.views import development2;
from courses.views import devops_mobile1;
from courses.views import devops_mobile2;
from courses.views import enroll_view;
from authentication.views import house;
from jobs.views import jobs;
from jobs.views import automation;
from jobs.views import booker;
from jobs.views import businessAnalyst;
from jobs.views import businessIntelligence;
from jobs.views import cyberSecurity;
from jobs.views import customerSupport;
from jobs.views import dataScientist;
from jobs.views import dataAnalyst;
from jobs.views import digitalMarketing;
from jobs.views import salesRepre;
from jobs.views import machineLearning;
from jobs.views import salesOperation;
from jobs.views import contentCreator;
from jobs.views import dataWarehouse;
from jobs.views import projectManager;
from jobs.views import humanResource;
from jobs.views import pythonDeveloper;
from jobs.views import pythonDeveloper;
from jobs.views import salesRepresentative;
from jobs.views import scrumMaster;
from jobs.views import userInterface;
from jobs.views import videoGame;
from jobs.views import jobsForm;
from jobs.views import fullStack;
from jobs.views import frontend;


urlpatterns = [
    # path('admin/', admin.site.urls),
   path('', indexPage, name='index'),           # Main Page
    path('auth/', authPage, name='auth'),        # Login/Register Page
    path('logout/', logout_view, name='logout'), # Logout
    path('dashboard/', dashboard, name='profile'),# Profile Page
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
 

    path('courses/',courses, name='courses'),   
    path('ai_data1/',ai_data1, name='ai_data1'),
    path('ai_data2/',ai_data2, name='ai_data2'),
    path('cyber_cloud1/',cyber_cloud1, name='cyber_cloud1'),
    path('cyber_cloud2/',cyber_cloud2, name='cyber_cloud2'),
    path('development1/',development1, name='development1'),
    path('development1/',development2, name='development2'),
    path('devops_mobile1/',devops_mobile1, name='devops_mobile1'),
    path('devops_mobile2/',devops_mobile2, name='devops_mobile2'),
    path('enroll',enroll_view, name='enroll'),

    path('jobs/',jobs, name='jobs'),
    path('automation/',automation, name='automation'),
    path('business-analyst/',businessAnalyst, name='businessAnalyst'),
    path('full-stack/',fullStack, name='fullStack'),
    path('frontend/',frontend, name='frontend'),
    path('booker/',booker, name='booker'),
    path('content-creator/',contentCreator, name='contentCreator'),
    path('customer-support/',customerSupport, name='customerSupport'),
    path('cyber-security/',cyberSecurity, name='cyberSecurity'),
    path('data-analyst/',dataAnalyst, name='dataAnalyst'),
    path('data-warehouse/',dataWarehouse, name='dataWarehouse'),
    path('data-scientist/',dataScientist, name='dataScientist'),
    path('digital-marketing/',digitalMarketing, name='digitalMarketing'),
    path('human-resource/',humanResource, name='humanResource'),
    path('machine-learning/',machineLearning, name='machineLearning'),
    path('project-manager/',projectManager, name='projectManager'),
    path('python-developer/',pythonDeveloper, name='pythonDeveloper'),
    path('sales-operation/',salesOperation, name='salesOperation'),
    path('sales-repre/',salesRepre, name='salesRepre'),
    path('sales-representative/',salesRepresentative, name='salesRepresentative'),
    path('scrum-master/',scrumMaster, name='scrumMaster'),
    path('user-interface/',userInterface, name='userInterface'),
    path('video-game/',videoGame, name='videoGame'),
    path('jobsForm/',jobsForm, name='jobsForm'),
    path('business-intelligence/',businessIntelligence, name='businessIntelligence')

]
