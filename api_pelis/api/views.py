from .models import Pelicula, PeliculaFavorita
from .serializers import PeliculaSerializer, PeliculaFavoritaSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, views, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PeliculaViewSet(viewsets.ModelViewSet):
  queryset = Pelicula.objects.all()
  serializer_class = PeliculaSerializer #This will transform to jason format
  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['titulo','estreno'] #Campos de busqueda en el filtro
  ordering_fields = ['favoritos']

class MarcarPeliculaFavorita(views.APIView): #This is a GenericAPI's view
  # To marking and dismarking user must be authenticaed
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

  #Buscamor el obj con la película a partir del identificador 'id' que pasamos en los datos
  # en ese diccionario 
    def post(self, request):
      pelicula = get_object_or_404(
        Pelicula, id=self.request.data.get('id', 0) #diccionario
      )

      """
        favorita : instacia creada
        created: valor booleano (ya existe o no la pelicula)

        si no existe , la marca como favorita si la encinta, existe 
        y la desmarca como favorita
      """
      favorita, created = PeliculaFavorita.objects.get_or_create(
        pelicula = pelicula, usuario=request.user
      )

        # Por defecto suponemos que se crea bien la instacia
      content = {
        'id': pelicula.id,
        'favorita': True
      }

      # Si no se ha creado es que ya existe, entonces borramos el favorito
      if not created:
        favorita.delete()
        content['favorita'] = False

      return Response(content)

class ListarPeliculasFavoritas(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

  # GET -> Se usa para hacer lecturas

    def get(self, request):
      peliculas_favoritas = PeliculaFavorita.objects.filter(
        usuario=request.user)
      serializer = PeliculaFavoritaSerializer(
        peliculas_favoritas, many=True)

      return Response(serializer.data)