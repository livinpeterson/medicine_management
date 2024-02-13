from django.shortcuts import render, redirect, HttpResponse
from medicine_management.models import Medicine
from medicine_management.forms import Medicineform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

# Create your views here.
@login_required(login_url='login')
def index(request):

    data = Medicine.objects.all()
    current_time = timezone.now()

    context = {
        'medicines': data,
        'current_time':current_time
    }

    return render(request, 'index.html', context)


@login_required(login_url='login')
def searchpage(request):
    if 'search' in request.GET:
        search=request.GET['search']
        data=Medicine.objects.filter(name__istartswith=search)
        context={
            'search': search,
            'medicines': data,
        }
    return render (request,'index.html',context)



def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirm_password')    

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "The Username and Email already exists")
            return redirect('signup')
        
        if password != confirmpassword:
            messages.error(request, "Your Password & Confirm Password are not same")
            return redirect('signup')

        if not username:
            messages.error(request, 'Enter the Username')
            return redirect('signup')

        else:
            my_User=User.objects.create_user(username, email, password)
            my_User.save()
            return redirect("login")
                
    return render (request,'signup.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, "User Name or Password is Incorrect.")
            return redirect('login')
    return render (request,'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        form = Medicineform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Medicineform
    context={
        'form': form
    }
    return render (request,'add.html',context)


@login_required(login_url='login')
def update(request, id):
    data = Medicine.objects.get(id=id)
    if request.method == "POST":
        form = Medicineform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Medicineform(instance=data)
    context={
        'form': form
    }
    return render (request,'update.html',context)


@login_required(login_url='login')
def delete(request, id):
    data = Medicine.objects.get(id=id)
    data.delete()
    return redirect('index')

