from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def authPage(request):
    return render(request,'auth.html')