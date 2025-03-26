import os
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Update movie images from folder"

    def handle(self, *args, **kwargs):
    
        # ✅ Folder to save images
        images_folder = 'media/movie/images/'
        os.makedirs(images_folder, exist_ok=True)

        # ✅ Fetch all movies
        movies = Movie.objects.all()
        self.stdout.write(f"Found {movies.count()} movies")

        for movie in movies:
            try:
                movie_title = movie.title

                # ✅ Prepare the filename and full save path
                image_filename = f"m_{movie_title}.png"

                # ✅ Call the helper function
                image_relative_path = os.path.join('movie/images', image_filename)

                # ✅ Update database
                movie.image = image_relative_path
                movie.save()
                self.stdout.write(self.style.SUCCESS(f"Saved and updated image for: {movie.title}"))

            except Exception as e:
                self.stderr.write(f"Failed for {movie.title}: {e}")

        self.stdout.write(self.style.SUCCESS("Process finished (only first movie updated)."))