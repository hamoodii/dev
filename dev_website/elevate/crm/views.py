from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


def homepage(request):
    return render(request, "crm/index.html")

def  register(reguest):
    return render(reguest, "crm/register.html")

def register1(reguest):
    return HttpResponse("this is the another registeration page")