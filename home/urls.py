from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name = "home"),
path('add_horse', views.add_horse, name="add-horse"),
path('add_race', views.add_race, name="add-race"),
path('add_expense', views.add_expense, name="add-expense"),

path('Horses', views.displayhorses, name="displayhorses"),
path('horses_sold', views.displayhorsesSold, name="displayhorsesSold"),
path('sell/<horse_id>', views.sell, name='sell'),
path('edit/<horse_id>', views.edit, name='edit'),
path('displayHorse/<horse_id>', views.displayHorse, name='displayHorse'),


path('racePage', views.racePage,name="racePage"),
path('expensePage', views.expensePage,name="expensePage"),


path('display_race', views.displayRace, name="display-race"),
path('display_expense', views.displayExpense, name = "display-expense"),
path('expense_per_month', views.expensePerMonth, name= "expense-per-month"),
]
