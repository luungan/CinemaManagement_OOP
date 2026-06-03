import json

from models.movie import Movie


class MovieService:
    def __init__(self):
        self.movie_list = []
        self.load_data()

   # Add movie
    def add_movie(self, movie):
         old_movie = self.find_movie_by_id(movie.movie_id)

         if old_movie is not None:
             print("Movie ID already exists")
             return False
         self.movie_list.append(movie)
         return True

    # Display all movies
    def display_movies(self):
        if len(self.movie_list) == 0:
            print("Movie list is empty")
            return

        for movie in self.movie_list:
            print(movie)

    # Find movie by ID
    def find_movie_by_id(self, movie_id):
        for movie in self.movie_list:
            if movie.movie_id == movie_id:
                return movie

        return None

    # Delete movie
    def delete_movie(self, movie_id):
        movie = self.find_movie_by_id(movie_id)

        if movie is not None:
            self.movie_list.remove(movie)
            return True

        return False
    
    # Update movie
    def update_movie(self, movie_id, new_title, new_genre, new_duration):
        movie = self.find_movie_by_id(movie_id)

        if movie is not None:
            movie.title = new_title
            movie.genre = new_genre
            movie.duration = new_duration

            return True
        
        return False
    
    # Sort movie by title
    def sort_by_title(self):
        self.movie_list.sort(key=lambda movie: movie.title)


    # Sort movie by duration descending
    def sort_by_duration_desc(self):
        self.movie_list.sort(
            key=lambda movie: movie.duration,
            reverse=True
        ) 

    # Save JSON
    def save_data(self):
        data = []

        for movie in self.movie_list:
            data.append(movie.to_dict())

        with open("data/movies.json", "w") as file:
            json.dump(data, file, indent=4)

    # Load JSON
    def load_data(self):
        try:
            with open("data/movies.json", "r") as file:
                data = json.load(file)

                for item in data:
                    movie = Movie(
                        item["movie_id"],
                        item["title"],
                        item["genre"],
                        item["duration"]
                    )

                    self.movie_list.append(movie)

        except:
            print("No movie data found")