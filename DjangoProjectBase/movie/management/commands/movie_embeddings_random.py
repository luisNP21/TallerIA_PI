import random
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Muestra los primeros valores del vector de embeddings de una película seleccionada al azar"

    def handle(self, *args, **kwargs):
        # Obtener todas las películas de la base de datos
        movies = Movie.objects.all()

        if not movies.exists():
            self.stdout.write(self.style.ERROR("No hay películas en la base de datos."))
            return

        # Seleccionar una película al azar
        random_movie = random.choice(movies)

        # Obtener los embeddings de la película
        try:
            if not random_movie.emb:
                self.stdout.write(self.style.WARNING(f"La película '{random_movie.title}' tiene embeddings vacíos o no definidos."))
                return

            # Convertir los embeddings a un vector numpy
            embedding_vector = np.frombuffer(random_movie.emb, dtype=np.float32)

            # Mostrar los primeros 5 valores del vector
            self.stdout.write(self.style.SUCCESS(f"Película seleccionada: {random_movie.title}"))
            self.stdout.write(f"Primeros valores del vector de embeddings: {embedding_vector[:5]}")
        except AttributeError:
            self.stdout.write(self.style.ERROR(f"La película '{random_movie.title}' no tiene un campo 'emb' definido."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error inesperado al obtener los embeddings: {e}"))