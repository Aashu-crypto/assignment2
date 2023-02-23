from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from rest_framework import permissions

from .decorators import unauthenticated_user,allowed_user
# Create your views here.

class HasPermission(permissions.BasePermission):
    """
    Allows access only to users who have the appropriate permission.
    """

    permission_codename = ""

    def __init__(self, permission_codename):
        super().__init__()
        self.permission_codename = permission_codename

    def __call__(self):
        return self

    def has_permission(self, request, view):
        return request.user.has_permission(self.permission_codename)
    

@login_required(login_url="login")
def index(request):
    
    return render(request,"index.html")

@unauthenticated_user
def register(request):
    form =  createUserform()
    
    if request.method == "POST":
        form =  createUserform(request.POST)
        if form.is_valid():
            user =form.save()
            group =Group.objects.get(name = "customer")
            user.groups.add(group)
            return redirect('login')
    context  = {'form':form}
    return render(request,"register.html",context)



def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username =username,password= password )
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,"login.html")


def logoutUser(request):
    logout(request)
    return redirect('login')



def products(request):
    return render(request,"products.html")


@allowed_user(allowed_roles=['admin','customer'])
def page2(request):
    
    return render(request,"page2.html")


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def page3(request):
    return render(request,"page3.html")

@login_required(login_url='login')
@permission_required("can_view_page4")
def page4(request):
    return render(request,"page4.html")



def page5(request):
    return render(request,"page5.html")


