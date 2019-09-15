from .models import Pelicula
from rest_framework import serializers

class PeliculaSerializer(serializers.ModelSerializer):
  class Meta:
    #Serlize he model Peliculas and all its fields
    model = Pelicula
    # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
    fields = '__all__'