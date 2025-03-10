from django.shortcuts import render, redirect
from app.models import *
import os
from django.http import HttpResponse

# Create your views here.

def home(req):
    return render(req, "home.html")

def account(req):
    return render(req, "account.html")

def order(req):
    return render(req, "order.html")

def cart(req):
    return render(req, "cart.html")

def decor(req):
    return render(req, "decor.html")

def elec(req):
    return render(req, "elec.html")

def sports(req):
    return render(req, "sports.html")

def cloth(req):
    return render(req, "cloth.html")

def jwel(req):
    return render(req, "jwel.html")

def beauty(req):
    return render(req, "beauty.html")
def signup(req):
    return render(req, "signup.html")
def login(req):
    return render(req, "login.html")

def log(req):
    a = req.GET['fullname']
    b = req.GET['password']
    if user.objects.filter(fullname =a, password = b):
        return render(req, 'home.html')
    else:
        return render(req, 'login.html')

def sign(request):
    u=user()
    u.fullname=request.GET['fullname']
    u.email=request.GET['email']
    u.password=request.GET['password']
    u.save() 
    return redirect("../login")

def edit(request,id):
    d=user.objects.get(id=id)
    return render(request,'edit.html',{'x':d})
def edcode(request,id):
    d=user.objects.get(id=id)
    d.fullname=request.GET['fullname']
    d.email=request.GET['email']
    d.password=request.GET['password']
    d.save()
    return redirect('../show')

def dele(request,id):
    d=user.objects.get(id=id)
    d.delete()
    return redirect("../show")


def show(request):
    a=user.objects.all()
    return render(request,'show.html',{'x':a})