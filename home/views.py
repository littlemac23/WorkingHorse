from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Horse, Race, Expense
from .filters import RaceFilter, ExpenseFilter
from .forms import CreateHorseForm, CreateRaceForm, CreateExpenseForm, SellHorseForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_horse(request):
    submitted = False
    if request.method =="POST":
        form = CreateHorseForm(request.POST)
        if form.is_valid():
            horse = form.save(commit=False)
            horse.user = request.user
            horse.save()
            return HttpResponseRedirect('/add_horse?submitted=True')
    else:
        form = CreateHorseForm
        if 'submitted' in request.GET:
            submitted = True

    #list = horseData.objects.all()

    return render(request, 'horse/add_horse.html',{'form':form, 'submitted': submitted, 'horsedata': list})


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

    return render(request, 'race/add_race.html',{'form':form, 'submitted': submitted, 'Race': list})


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

    return render(request, 'expense/add_expense.html',{'form':form, 'submitted': submitted, 'Expense': list})

#Displays list of horses
def displayhorses(request):
    horses = Horse.objects.filter(user=request.user.id, sold=False )
    return render(request, 'Horse/Horses.html',
    {'horses': horses})
#Displays information for one horse
def displayHorse(request, horse_id):
    horse = Horse.objects.get(pk=horse_id)
    return render(request, 'Horse/display_horse.html',
    {'horse': horse})


def displayhorsesSold(request):
    horses = Horse.objects.filter(user=request.user.id, sold=True )
    return render(request, 'Horse/horses_sold.html',
    {'horses': horses})


@login_required
def displayRace(request):
    race_list = Race.objects.filter(name__user=request.user)

    myFilter = RaceFilter(request.GET, queryset=race_list)
    race_list = myFilter.qs

    return render(request, 'race/display_race.html',
    {'race_list': race_list, 'myFilter': myFilter})


@login_required
def displayExpense(request):
    expense_list = Expense.objects.filter(name__user=request.user)

    myFilter = ExpenseFilter(request.GET, queryset=expense_list)
    expense_list = myFilter.qs

    return render(request, 'expense/display_expense.html',
    {'expense_list': expense_list,  'myFilter': myFilter})


def expensePerMonth(request):
    qs = Expense.objects.all()
    name_contains_query = request.GET.get('name_contains')
    decription_contains_query = request.GET.get('decription_containss')
    context = {
        'queryset': qs
    }
    return render(request, 'expense/expense_per_month.html', context)




def racePage(request):
    return render(request, 'race/racePage.html', {})

def expensePage(request):
    return render(request, 'Expense/expensePage.html', {})


def home(request):
    return render(request, 'home/Home.html', {})


def edit(request, horse_id):
    horse = Horse.objects.get(pk=horse_id)
    form = CreateHorseForm(request.POST or None, instance = horse)
    if form.is_valid():
        form.save()
        return redirect('displayhorses')
    return render(request, 'Horse/edit.html', {'form': form, 'horse': horse})

def edit_race(request, race_id):
    race = Race.objects.get(pk=race_id)
    form = CreateRaceForm(request.POST or None, instance = race)
    if form.is_valid():
        form.save()
        return redirect('display_race')
    return render(request, 'race/edit_race.html', {'form': form, 'race': race})


# View function for handling the horse selling process
# This function:
# 1. Displays a form for entering the selling price
# 2. Automatically marks the horse as sold when form is submitted
# 3. Redirects to the horses list after successful submission
def sell(request, horse_id):
    # Get the horse object by its ID
    horse = Horse.objects.get(pk=horse_id)
    
    # Create the form instance with POST data if provided
    form = SellHorseForm(request.POST or None, instance = horse)
    
    # Process the form if it's valid
    if form.is_valid():
        # Use commit=False to get the object without saving yet
        # This allows us to modify fields before final save
        horse_obj = form.save(commit=False)
        
        # Automatically set sold status to True
        # The user doesn't need to check a box - it happens automatically
        # when the update button is clicked
        horse_obj.sold = True
        
        # Save the horse with updated fields
        horse_obj.save()
        
        # Redirect to the horses list page
        return redirect('displayhorses')
        
    # If form not submitted or invalid, display the form
    # Uses sell_horse.html template to render the form
    return render(request, 'Horse/sell_horse.html', {'form': form, 'horse': horse})
