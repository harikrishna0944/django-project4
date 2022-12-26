from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("<h1>first view of app1</h1>")
def second(request):
    return HttpResponse("<h1>second view of app1</h1>")

