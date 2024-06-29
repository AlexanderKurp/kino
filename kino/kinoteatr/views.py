from django.shortcuts import render, get_object_or_404
from .models import Movie, Session, Ticket
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/index.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'cinema/movie_detail.html', {'movie': movie})

def session_detail(request, pk):
    session = get_object_or_404(Session, pk=pk)
    return render(request, 'cinema/session_detail.html', {'session': session})

@login_required
def book_ticket(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    seat = request.POST.get('seat')
    Ticket.objects.create(user=request.user, session=session, seat=seat)
    return HttpResponseRedirect(reverse('session_detail', args=[session_id]))