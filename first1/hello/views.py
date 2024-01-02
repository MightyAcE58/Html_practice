from django.shortcuts import render
from django.http import HttpResponce
# Create your views here.
def index(request):
    return HttpResponce("hello,world") 
