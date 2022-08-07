from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name = "home"),
path('add_horse', views.add_horse, name="add-horse"),
path('add_race', views.add_race, name="add-race"),
path('add_expense', views.add_expense, name="add-expense"),

path('Horses', views.displayhorses, name="displayhorses"),
path('Horse/horses_sold', views.displayhorsesSold, name="displayhorsesSold"),
path('Horse/sell/<horse_id>', views.sell, name='sell'),
path('Horse/edit/<horse_id>', views.edit, name='edit'),
path('Horse/displayHorse/<horse_id>', views.displayHorse, name='displayHorse'),


path('race/racePage', views.racePage,name="racePage"),
path('race/edit_race/<race_id>', views.edit_race, name='edit_race'),
path('race/display_race', views.displayRace, name="display_race"),

path('expense/expensePage', views.expensePage,name="expensePage"),
path('expense/display_expense', views.displayExpense, name = "display_expense"),
]
