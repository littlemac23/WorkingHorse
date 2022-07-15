from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Horses.html', {})
def addhorse(request):
        return render(request, 'test.html', {})

def PostHorse(request, song_id):
        if request.method == 'POST':
            form = CreateCommentForm(request.POST)
            if form.is_valid():
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
