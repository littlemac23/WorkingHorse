from django.shortcuts import render
from django.http import HttpResponse
from .models import horseData

def home(request):
    return render(request, 'Horses.html', {})
def addhorse(request):
        return render(request, 'test.html', {})

def showHorse(request):
        list = horseData.objects.all()
        return render(request,'test.html', {'horsedata': list})

def PostHorse(request, song_id):
        if request.method == 'POST':

            form = CreateHorseForm(request.POST)
            if form.is_valid():

                name = models.TextField(max_length=500, primary_key=True)
                acquisitionDate = models.DateField()
                totalAcquisitionAmount = models.IntegerField()
                type = models.TextField(max_length=500)
                place = models.TextField(max_length=500)
                dispersmentClaim_Sale = models.IntegerField()
                dispersmentDate = models.DateField()



                body = request.POST.get('body', '')
                author = request.user
                time = datetime.datetime.now()
                SongName = song
                SongComment.objects.create(author = author,  time = time, SongName= SongName , body = body)
            return redirect('comments' , song)
            #return HttpResponseRedirect(request.path_info)

        post = SongComment.objects.all()
        form = CreateSongCommentForm()
        return render(request, 'comments.html', { 'song': song, 'form': form,  'post': post, 'name': name, 'likes':likes, 'dislikes':dislikes, 'percent':percent +"%", 'color':color, 'total':total , 'artists': artists, 'release_date': release_date})

# Create your views here.
