from django.shortcuts import render, get_object_or_404
from .models import Movie, Session, Ticket, Actor
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# регистрация
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import NewUser, AuthenticationUser, TicketBooking
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


def index(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/index.html', {'movies': movies})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'cinema/movie_detail.html', {'movie': movie})


def movie_sessions(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    sessions = Session.objects.filter(movie=movie)
    return render(request, 'cinema/movie_sessions.html', {'movie': movie, 'sessions': sessions})


def session_detail(request, pk):
    session = get_object_or_404(Session, pk=pk)
    return render(request, 'cinema/session_detail.html', {'session': session})


@login_required
def book_ticket(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    if request.method == 'POST':
        form = TicketBooking(request.POST)
        if form.is_valid():
            # Проверка наличия места
            seat = form.cleaned_data['seat']
            if not Ticket.objects.filter(session=session, seat=seat).exists():
                ticket = form.save(commit=False)
                ticket.user = request.user
                ticket.session = session
                ticket.save()
                return HttpResponseRedirect(reverse('session_detail', args=[session_id]))
            else:
                form.add_error('seat', 'Это место уже занято.')
    else:
        form = TicketBooking()

    return render(request, 'cinema/book_ticket.html', {'form': form, 'session': session})


def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, 'cinema/actor_detail.html', {'actor': actor})


def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'cinema/actors.html', {'actors': actors})


class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = NewUser
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginUser(LoginView):
    template_name = 'registration/login.html'
    success_url = '/'


class LogoutUser(LogoutView):
    next_page = reverse_lazy('index')
