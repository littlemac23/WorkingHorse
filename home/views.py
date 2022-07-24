from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Horse, Race, Expense
from .forms import CreateHorseForm, CreateRaceForm, CreateExpenseForm


def add_horse(request):
    submitted = False
    if request.method =="POST":
        form = CreateHorseForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            response.user.horse_set.create(name=n)
            return HttpResponseRedirect('/add_horse?submitted=True')
    else:
        form = CreateHorseForm
        if 'submitted' in request.GET:
            submitted = True

    #list = horsedata.objects.all()

    return render(request, 'Horse/add_horse.html',{'form':form, 'submitted': submitted, 'Horse': list})







def add_race(request):
    submitted = False
    if request.method =="POST":
        form = CreateRaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_race?submitted=True')
    else:
        form = CreateRaceForm
        if 'submitted' in request.GET:
            submitted = True

    #list = horsedata.objects.all()

    return render(request, 'Race/add_race.html',{'form':form, 'submitted': submitted, 'Race': list})


def add_expense(request):
    submitted = False
    if request.method =="POST":
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/add_expense?submitted=True')
    else:
        form = CreateExpenseForm
        if 'submitted' in request.GET:
            submitted = True

    #list = expensedata.objects.all()

    return render(request, 'Expense/add_expense.html',{'form':form, 'submitted': submitted, 'Expense': list})





def racePage(request):
    return render(request, 'Race/racePage.html', {})

def expensePage(request):
    return render(request, 'Expense/expensePage.html', {})


def home(request):
    return render(request, 'home/Home.html', {})
def addhorse(request):
        return render(request, 'Horse/test.html', {})

def showHorse(request):
        list = horsedata.objects.all()
        return render(request,'Horse/test.html', {'horsedata': list})

def Horse(request):
    if request.method =="POST":
        form = CreateHorseForm(request.POST)
        if form.is_valid():
            form.save()
            horsedata.objects.Create(form)
            return redirect("/horse")

    else:
        form = CreateHorseForm()

    list = horsedata.objects.all()
    return render(request,'Horse/test.html', {'horsedata': list}, {"form": form})
    #Sreturn render(request, "Horse/Horses.html", {"form": form})
