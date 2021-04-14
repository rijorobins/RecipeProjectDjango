from django.shortcuts import render,redirect
from users.forms import RegistrationUserForm,LoginForm,ProfileCreateForm
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Index(request):
    return render(request,"users/base.html")
def Register(request):
    form = RegistrationUserForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"users/login.html")
        else:
            print("hello")
            context["form"] = RegistrationUserForm(request.POST)
            return render(request,"users/registration.html",context)
    return render(request, "users/registration.html", context)
def signIn(request):
    form = LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username = username,password = password)
            if user:
                login(request,user)
                return render(request, "users/home.html")
            else:
                return render(request, "users/login.html")
    return render(request,"users/login.html",context)

def signOut(request):
    logout(request)
    return redirect("signin")

def userHome(request):
    return render(request,"users/home.html")

def create_profile(request):
    form = ProfileCreateForm(initial={"user":request.user})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProfileCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context["form"] = form
            return render(request, "users/createprofile.html", context)
    return render(request,"users/createprofile.html",context)

def edit_profile(request):
    user = Profile.objects.get(user=request.user)
    form = ProfileCreateForm(initial={"user":request.user},instance=user)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProfileCreateForm(instance=user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context["form"] = form
            return render(request,"users/editprofile.html",context)
    return render(request,"users/editprofile.html",context)

def view_profile(request):
    user = Profile.objects.get(user=request.user)
    context={}
    context["user"] = user
    return render(request,"users/viewprofile.html",context)

