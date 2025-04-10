from django.shortcuts import render

# Create your views here.
def jobs(request):
    return render(request,'jobs.html')

def automation(request):
    return render(request,'Automation.html')


def booker(request):
    return render(request,'Booker.html')


def businessAanalyst(request):
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

def jobsForm(request):
    return render(request,'jobs_form.html')
