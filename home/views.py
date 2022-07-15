from django.shortcuts import render
from django.http import HttpResponse
from .models import horseData
from .forms import CreateHorseForm

def home(request):
    return render(request, 'Horses.html', {})
def addhorse(request):
        return render(request, 'test.html', {})

def showHorse(request):
        list = horseData.objects.all()
        return render(request,'test.html', {'horsedata': list})

def PostHorse(request):
        if request.method == 'POST':

            form = CreateHorseForm(request.POST)
            if form.is_valid():

                name = request.POST.get("name")
                acquisitionDate = request.POST.get("acquisitionDate")
                totalAcquisitionAmount = request.POST.get("totalAcquisitionAmount")
                type = request.POST.get("type")
                place = request.POST.get("place")
                instance = PostHorse(name=name, acquisitionDate=acquisitionDate, totalAcquisitionAmount=totalAcquisitionAmount,type=type, place=place)
                instance.save()
                #dispersmentClaim_Sale = request.POST.get("dispersmentClaim_Sale")
                #dispersmentDate = request.POST.get("dispersmentDate")

        #post = horseData.objects.all()
        #form = CreateHorseForm()
        #return render(request, 'Horse.html', { 'name': name, 'acquisitionDate': acquisitionDate,  'totalAcquisitionAmount': totalAcquisitionAmount, 'type': type,
        #'place':place, 'dispersmentClaim_Sale':dispersmentClaim_Sale, 'dispersmentDate':dispersmentDate})
        return render(request, "home/Horses.html", {"form": form})
# Create your views here.
