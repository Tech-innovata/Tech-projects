from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Student,Register


# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass1']
        confirmpassword = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"username already exist! Please try some other username")
            return redirect('home')
       
        if User.objects.filter(email=email):
            messages.error(request,"email already registered! Please register another email")
            return redirect('home')
        
        if len(username)<6:
            messages.error(request,"username must be 6 characters and above")
            return redirect('signup')
        
        if len(password)<4:
            messages.error(request,"password must be 6 characters and above")
            return redirect('signup')

        if password != confirmpassword:
            messages.error(request,"password didn't match!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request,"username must be Aplha-Numeric!")
            return redirect('home')
        
        if not password.isalnum():
            messages.error(request,"password must be Aplha-Numeric!")
            return redirect('signup')
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        
        messages.success(request,"Your account has been created successfully, we have sent an email code for you to activate your email")
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
           # surnname = user.fist_name
            return redirect('homepage')
        else:
            messages.error(request,"username or password incorrect")
            return redirect('signin')


    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')

def homepage(request):
    students=Student.objects.all()
    return render(request,'homepage.html',{'students':students})

def joinus_page(request):
    if request.method =='POST':
        student=Register(
           surname = request.POST['surname'],
           givenname = request.POST['givenname'],
           program = request.POST['program'],
           yearofstudy = request.POST['year'],
           school = request.POST['school'],
           parent = request.POST['parent'])
        student.save()
        return redirect('home')
    return render(request,'joinus.html')