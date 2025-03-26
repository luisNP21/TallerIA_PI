import os
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = 'Asigna imágenes a las películas desde la carpeta media/movie/images/'

    def handle(self, *args, **kwargs):
        # Ruta de la carpeta de imágenes
        images_folder = 'media/movie/images/'

        # Verificar si la carpeta existe
        if not os.path.exists(images_folder):
            self.stdout.write(self.style.ERROR(f'La carpeta {images_folder} no existe.'))
            return

        # Recorrer las películas en la base de datos
        movies = Movie.objects.all()
        for movie in movies:
            # Buscar una imagen que coincida con el título de la película
            image_name = f"{movie.title}.jpg"
            image_path = os.path.join(images_folder, image_name)

            if os.path.exists(image_path):
                # Actualizar la ruta de la imagen en la base de datos
                movie.image = image_path
                movie.save()
                self.stdout.write(self.style.SUCCESS(f'Imagen asignada a la película: {movie.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'No se encontró imagen para la película: {movie.title}'))

        self.stdout.write(self.style.SUCCESS('Proceso completado.'))