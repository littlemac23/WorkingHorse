from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name = "home"),
path('add_horse', views.add_horse, name="add-horse"),
path('add_race', views.add_race, name="add-race"),
path('add_expense', views.add_expense, name="add-expense"),


path('racePage', views.racePage,name="racePage"),
path('expensePage', views.expensePage,name="expensePage"),
]
