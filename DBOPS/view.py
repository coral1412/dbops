from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from dbopsModel.models import *
# from django.template.loader import render_to_string
import  os

def hello(request):
    return HttpResponse("hello world!")

def dbuserinfo_list(request):
    users=dbuserinfo.objects.all()
    return render(request,'userinfo.html',{'users':users})