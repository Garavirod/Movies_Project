# from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
# Working with signals
from django.db.models.signals import post_delete, post_save

class Pelicula(models.Model):
  titulo = models.CharField(max_length=150)
  estreno = models.IntegerField(default=2000)
  imagen = models.URLField(help_text="De imdb mismo")
  resumen = models.TextField(help_text="Descripción corta")
  favoritos = models.IntegerField(default=0)
  # LAs peliculas serán oordendas alfabeticamente por el titulo
  class Meta:
    ordering = ['titulo']


class PeliculaFavorita(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

# Working wuth signals
def update_favoritos(sender, instance, **kwargs):
  # We count the numner of relation which it has got with Favorite movie
  # Whith 'favoriye moive' we access to movies relation
  count = instance.pelicula.peliculafavorita_set.all().count() 
  instance.pelicula.favoritos = count
  instance.pelicula.save()


# en el post delete se pasa la copia de la instance que ya no existe
post_save.connect(update_favoritos, sender=PeliculaFavorita)
post_delete.connect(update_favoritos, sender=PeliculaFavorita)  