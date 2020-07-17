from django.http import HttpResponse
from django.shortcuts import render#(print data)

#create views here
#create with html response
from django.http import HttpResponse
def index(request):
    return HttpResponse("hello world")#HttpResponse(HTML tag as an argument)
def home(request):
    return HttpResponse("<h1> welcome to  django page</h1>")
def html_demo1(request):
    return render(request,"sample.html")
