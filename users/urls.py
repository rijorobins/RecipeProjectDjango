"""RecipeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from users.views import Register,signIn,signOut,create_profile,userHome,edit_profile,view_profile,Index



urlpatterns = [
    path("",Index,name="index"),
    path("registration",Register,name="registration"),
    path("login",signIn,name="signin"),
    path("logout",signOut,name="signout"),
    path("profile",create_profile,name="createprofile"),
    path("home",userHome,name="home"),
    path("editprofile",edit_profile,name="editprofile"),
    path("viewprofile",view_profile,name="viewprofile"),
]
