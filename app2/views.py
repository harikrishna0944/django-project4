from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hari(request):
    return HttpResponse("<h1>hari view of app2</h1>")
def krishna(request):
    return HttpResponse("<h1>krishna view of app2</h1>")

