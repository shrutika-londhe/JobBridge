from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Enrollment
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


def enroll_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('courseSelect')
        experience = request.POST.get('experience')
        payment_method = request.POST.get('paymentMethod')
        card_number = request.POST.get('cardNumber', '')
        card_name = request.POST.get('cardName', '')
        expiry_date = request.POST.get('expiryDate', '')
        cvv = request.POST.get('cvv', '')
        paypal_email = request.POST.get('paypalEmail', '')
        upi_id = request.POST.get('upiId', '')

        enrollment = Enrollment(
            full_name=full_name,
            email=email,
            phone=phone,
            course=course,
            experience=experience,
            payment_method=payment_method,
            card_number=card_number,
            card_name=card_name,
            expiry_date=expiry_date,
            cvv=cvv,
            paypal_email=paypal_email,
            upi_id=upi_id,
        )
        enrollment.save()

        messages.success(request, 'Enrollment successful!')
        return redirect('index')

    return render(request, 'enroll.html')
