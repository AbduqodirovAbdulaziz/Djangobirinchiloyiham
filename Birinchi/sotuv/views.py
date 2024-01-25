from django.shortcuts import render
from django.http import HttpResponse

def salomlash(request):
    return HttpResponse("<h1>Salom,Abdulaziz tanishganimdan hursandman!</h1>")

def bosh_sahifa(req):
    return render(req, "Boqcha.html")

def cristiano(req):
    return render(req, "cristiano.html")