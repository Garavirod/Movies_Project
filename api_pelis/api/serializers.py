from .models import Pelicula, PeliculaFavorita
from rest_framework import serializers

class PeliculaSerializer(serializers.ModelSerializer):
  class Meta:
    #Serlize he model Peliculas and all its fields
    model = Pelicula
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'

class PeliculaFavoritaSerializer(serializers.ModelSerializer):
      
  pelicula = PeliculaSerializer() #Seralizamos el campo pelicula  a partir del serizalizdor de arriba

  class Meta:
    model = PeliculaFavorita
    fields = ['pelicula'] #Seralizará el campo película