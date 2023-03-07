from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def akhif(request):
    return HttpResponse('<h1><marquee>akhif loves deepthi</marquee></h1>')
def balu(request):
    return HttpResponse('<h1><center>Balu loves akhila</center></h1>')