from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('contact')

def tracker(request):
    return HttpResponse('tracker')

def search(request):
    return HttpResponse('search')

def productview(request):
    return HttpResponse('productview')

def checkout(request):
    return HttpResponse('checkout')



