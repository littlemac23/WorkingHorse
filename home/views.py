from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Horses.html', {})
def addhorse(request):
        return render(request, 'test.html', {})
# Create your views here.
