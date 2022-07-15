from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import horseData
from .forms import CreateHorseForm

def home(request):
    return render(request, 'Horse/Horses.html', {})
def addhorse(request):
        return render(request, 'Horse/test.html', {})

def showHorse(request):
        list = horseData.objects.all()
        return render(request,'Horse/test.html', {'horsedata': list})

def Horse(request):
    if request.method =="POST":
        form = CreateHorseForm(request.POST)
        if form.isValid():
            form.save()
            return redirect("/")
    else:
        form = CreateHorseForm()
    return render(request, "Horse/Horses.html", {"form": form})
