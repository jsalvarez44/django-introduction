from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse("Hello World!")

def simpleReturn(request):
    msg = 1 + 1
    return HttpResponse(str(msg))

def simpleHTML(request):
    html = '<h1>Hello World! in HTML :)</h1>'
    return HttpResponse(str(html))
