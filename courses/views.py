from django.shortcuts import render

# Create your views here.

def courses(request):
    return render(request,'course.html')

def ai_data1(request):
    return render(request,'ai_data1.html')

def ai_data2(request):
    return render(request,'ai_data2.html')

def cyber_cloud1(request):
    return render(request,'cyber_cloud1.html')

def cyber_cloud2(request):
    return render(request,'cyber_cloud2.html')

def development1(request):
    return render(request,'development1.html')

def development2(request):
    return render(request,'development2.html')

def devops_mobile1(request):
    return render(request,'devops_mobile1.html')

def devops_mobile2(request):
    return render(request,'devops_mobile2.html')

def enroll(request):
    return render(request,'enroll.html')