from django.shortcuts import render

# Create your views here.
def jobs(request):
    return render(request,'jobs.html')

def automation(request):
    return render(request,'Automation.html')


def booker(request):
    return render(request,'Booker.html')

def fullStack(request):
    return render(request, 'Full_stack.html')

def frontend(request):
    return render(request, 'Frontend.html')

def businessAnalyst(request):
    return render(request,'Business_Analyst.html')

def businessIntelligence(request):
    return render(request,'Business_Intelligence.html')

def contentCreator(request):
    return render(request,'Content_Creator.html')

def customerSupport(request):
    return render(request,'Customer_Support.html')

def cyberSecurity(request):
    return render(request,'cyber_security.html')

def dataAnalyst(request):
    return render(request,'Data_Analyst.html')

def dataWarehouse(request):
    return render(request,'Data_warehouse.html')

def dataScientist(request):
    return render(request,'Data_scientist.html')

def digitalMarketing(request):
    return render(request,'Digital_Marketing.html')

def humanResource(request):
    return render(request,'HumanResource.html')
    
def machineLearning(request):
    return render(request,'Machine_learning.html')
    
def projectManager(request):
    return render(request,'Project_Manager.html')
    
def pythonDeveloper(request):
    return render(request,'pythonDeveloper.html')

def salesOperation(request):
    return render(request,'sales_operation.html')

def salesRepre(request):
    return render(request,'sales_repre.html')

def salesRepresentative(request):
    return render(request,'sales_representative.html')

def scrumMaster(request):
    return render(request,'scrumMaster.html')

def userInterface(request):
    return render(request,'User_interface.html')

def videoGame(request):
    return render(request,'VideoGame.html')

from django.shortcuts import render, redirect
from .models import JobApplication

def jobsForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        resume = request.FILES.get('resume')
        message = request.POST.get('message')

        job = JobApplication(
            name=name,
            email=email,
            phone=phone,
            dob=dob,
            address=address,
            gender=gender,
            position=position,
            resume=resume,
            message=message
        )
        job.save()
        return redirect('index')  # redirect to home or a success page

    return render(request, 'jobs_form.html')
