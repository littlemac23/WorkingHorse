from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Horse, Race, Expense
from .forms import CreateHorseForm, CreateRaceForm, CreateExpenseForm


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
    race_list = Race.objects.all()
    return render(request, 'Race/display_race.html',
    {'race_list': race_list})




def testing(request):
  expense_list = Expense.objects.filter(decription='Farm').values()
  template = loader.get_template('home/Home.html')
  context = {
    'expense_list': expense_list,
  }
  return HttpResponse(template.render(context, request))



# Check out template.html to see how the mymembers object
# was used in the HTML code.







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
