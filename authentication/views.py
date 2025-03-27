from django.shortcuts import render, redirect
import mysql.connector as sql

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'AboutUs.html')

def contact(request):
    return render(request,'contactUs.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def authPage(request):
    if request.method == 'POST':
        action = request.POST.get('action')  # Check if login or register
        obj = sql.connect(host="localhost", user="root", password="system", database="jobridge")
        cursor = obj.cursor()

        if action == "login":
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            # Ensure correct table name (users, not auth_user)
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
            result = cursor.fetchone()

            cursor.close()
            obj.close()

            if result:
                return render(request, 'index.html', {'message': 'Login successful!'})
            else:
                return render(request, 'auth.html', {'message': 'User does not exist. Please sign up!'})

        elif action == "register":
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            # Check if user already exists in 'users' table
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                cursor.close()
                obj.close()
                return render(request, 'auth.html', {'message': 'User already exists. Please log in!'})

            # Insert new user into 'users' table
            cursor.execute("INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)",
                           (firstname, lastname, email, password))
            obj.commit()

            cursor.close()
            obj.close()

            return render(request, 'index.html', {'message': 'User registered successfully! Please log in.'})

    return render(request, 'auth.html')

