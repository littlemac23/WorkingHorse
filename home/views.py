from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import horseData
from .forms import CreateHorseForm


def add_horse(request):
    submitted = False
    if request.method =="POST":
        form = CreateHorseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_horse?submitted=True')
    else:
        form = CreateHorseForm
        if 'submitted' in request.GET:
            submitted = True

<<<<<<< HEAD
    list = horseData.objects.all()
=======
        list = horseData.objects.all()
>>>>>>> 9517ca154f34098c133ad2aaf1d3879010c472fe

    return render(request, 'Horse/add_horse.html',{'form':form, 'submitted': submitted, 'horsedata': list})



<<<<<<< HEAD
def racePage(request):
    return render(request, 'racePage.html', {})

def expensePage(request):
    return render(request, 'expensePage.html', {})
=======
>>>>>>> 9517ca154f34098c133ad2aaf1d3879010c472fe



def home(request):
    return render(request, 'Home.html', {})
def addhorse(request):
        return render(request, 'Horse/test.html', {})

def showHorse(request):
        list = horseData.objects.all()
        return render(request,'Horse/test.html', {'horsedata': list})

def Horse(request):
    if request.method =="POST":
        form = CreateHorseForm(request.POST)
        if form.is_valid():
            form.save()
            horseData.objects.Create(form)
            return redirect("/horse")

    else:
        form = CreateHorseForm()

    list = horseData.objects.all()
    return render(request,'Horse/test.html', {'horsedata': list}, {"form": form})
    #Sreturn render(request, "Horse/Horses.html", {"form": form})
