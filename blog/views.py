from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def storyone(request):
    return render(request, 'blog/storyone.html')
