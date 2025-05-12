from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def create_user_defaul():
    if not User.objects.filter(username='1234').exists():
        User.objects.create_user(username='1234', password='1234')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = requeste.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('movie_list')
    else:
        messages.error(request, "Credentdials isn't found it")

    return render(request, 'login.html')

