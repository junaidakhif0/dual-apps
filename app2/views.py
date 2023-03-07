from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def haroon(request):
    return HttpResponse('<h1>I love my brother</h1>')
def shafi(request):
    return HttpResponse('<h1>i love my brother</h1>')