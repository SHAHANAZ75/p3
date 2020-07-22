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
def second(request):
    return render(request,"directory/second.html")
def third(request):
    return render(request,"directory/third.html",context={'data':"shanu",'name':"Lucky"}) 
def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{'fruits':fruits})  
def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':5})
def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))
def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))
def ab(request, ab):
    gre=list(map(int,ab.split(" ")))
    return HttpResponse(f"<h1> Maximum num is:{max(gre)}</h1>")

def gre(request,num):
    a=num.split(" ")
    if int(a[0])>int(a[1]):
        gre=int(a[0])
    else:
        gre=int(a[1])
    res=gre
    return HttpResponse(str(res))