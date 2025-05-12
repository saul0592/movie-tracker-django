from django import forms
from .models import Movie
from django.apps import AppConfig

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'year', 'rating', 'watched']

from django.apps import AppConfig

class MoviesConfig(AppConfig):  # Asegúrate que el nombre coincida con INSTALLED_APPS
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'

    def ready(self):
        from .views import crear_usuario_por_defecto
        crear_usuario_por_defecto()