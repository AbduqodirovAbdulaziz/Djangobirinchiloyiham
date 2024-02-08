from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.http import HttpResponse


def salomlash(request):
    return HttpResponse("<h1>Salom,Abdulaziz tanishganimdan hursandman!</h1>")


def bosh_sahifa(req):
    return render(req, "Boqcha.html")


def cristiano(req):
    return render(req, "cristiano.html")


def editNazoratchi(request):
    context = {
        "nazoratchi": Nazoratchi.objects.all()
    }
    return render(request, 'edit_Nazoratchi.html', context)


def edit_Oqituvchi(requests, id):
    if requests.method == "POST":
        nazoratchi = Nazoratchi.objects.get(id=id)
        nazoratchi.ism = requests.POST["ism"]
        nazoratchi.kasb = requests.POST["kasb"]
        # nazoratchi.imtixon = Imtixon.objects.get(id=requests.POST['imtixon'])
        nazoratchi.save()

        return redirect('/editNazoratchi/')
    contex = {
        'nazoratchi': Nazoratchi.objects.get(id=id)
    }
    return render(requests, 'edit_Oqituvchi.html', contex)


def hamma_kurslar(requests):
    context = {
        "kurslar": Kurs.objects.all()
    }
    return render(requests, 'hamma_kurslar.html', context)


def kursni_tahrirlash(request, id):
    if request.method == "POST":
        kurslar = Kurs.objects.get(id=id)
        kurslar.nom = request.POST['nom']
        kurslar.daraja = request.POST['daraja']
        kurslar.narx = request.POST['narx']
        kurslar.chegirma = request.POST['chegirma']
        kurslar.save()
        return redirect('/hamma_kurslar/')

    context = {
        "kurslar": Kurs.objects.get(id=id)
    }
    return render(request, 'edit_kurslar.html', context)


def hamma_fanlar(request):
    context = {
        "fanlar": Fan.objects.all()
    }
    return render(request, 'hamma_fan.html', context)


def fanlar_edit(request, id):
    if request.method == "POST":
        fanlar = Fan.objects.get(id=id)
        fanlar.nomi = request.POST['nomi']
        fanlar.oqituvchi = Ustoz.objects.get(id=request.POST['oqituvchi'])
        fanlar.credit = request.POST['credit']
        fanlar.save()
        return redirect('/hamma_fanlar/')

    context = {
        "fanlar": Fan.objects.get(id=id),
        "ustozlar": Ustoz.objects.all()
    }
    return render(request, 'edit_fan.html', context)


# --------------------------------------------------------------
def fan_add(request):
    if request.method == "POST":
        data = FanForm(request.POST)
        if data.is_valid():
            Fan.objects.create(
                nomi=data.cleaned_data["nomi"],
                oqituvchi=data.cleaned_data["oqituvchi"],
                credit=data.cleaned_data["credit"],
            )
        return redirect("/fan_add/")
    context = {
        "fanlar": Fan.objects.all(),
        "form": FanForm
    }
    return render(request, 'hamma_fan.html', context)


# ---------------------------------------------------------------

def ustoz_add(request):
    if request.method == "POST":
        data = UstozForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/ustoz_add/')
    context = {
        "ustozlar": Ustoz.objects.all(),
        "form": UstozForm()
    }
    return render(request, 'hamma_ustozlar.html', context)

# -----------------------------------------------------------------
def kurs_add(request):
    if request.method=="POST":
        data=KursForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/kurs_add/')

    context={
        "kurslar": Kurs.objects.all(),
        "form": KursForm()
    }
    return render(request,'hamma_kurslar.html',context)