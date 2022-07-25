from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Horse, Race, Expense
from .forms import CreateHorseForm, CreateRaceForm, CreateExpenseForm
from django.contrib.auth.models import User

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

    #list = horseData.objects.all()

    return render(request, 'Horse/add_horse.html',{'form':form, 'submitted': submitted, 'horsedata': list})






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



def displayRace(request):
    race_list = Race.objects.filter(name_id=request.user.id)
    return render(request, 'Race/display_race.html',
    {'race_list': race_list})

def displayExpense(request):
    expense_list = Expense.objects.all()
    return render(request, 'home/Home.html',
    {'expense_list': expense_list})




def racePage(request):
    return render(request, 'Race/racePage.html', {})

def expensePage(request):
    return render(request, 'Expense/expensePage.html', {})


def home(request):
    return render(request, 'home/Home.html', {})
