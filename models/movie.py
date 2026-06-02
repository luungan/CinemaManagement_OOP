class Movie:
    def __init__(self, movie_id, title, genre, duration):
        self.__movie_id = movie_id
        self.__title = title
        self.__genre = genre
        self.__duration = duration

    # Getter movie_id
    @property
    def movie_id(self):
        return self.__movie_id

    # Setter movie_id
    @movie_id.setter
    def movie_id(self, value):
        self.__movie_id = value

    # Getter title
    @property
    def title(self):
        return self.__title

    # Setter title
    @title.setter
    def title(self, value):
        self.__title = value

    # Getter genre
    @property
    def genre(self):
        return self.__genre

    # Setter genre
    @genre.setter
    def genre(self, value):
        self.__genre = value

    # Getter duration
    @property
    def duration(self):
        return self.__duration

    # Setter duration
    @duration.setter
    def duration(self, value):
        if value <= 0:
            raise ValueError("Duration must be greater than 0")
        self.__duration = value

    def to_dict(self):
        return {
            "movie_id": self.__movie_id,
            "title": self.__title,
            "genre": self.__genre,
            "duration": self.__duration
        }

    def __str__(self):
        return f"{self.__movie_id} | {self.__title} | {self.__genre} | {self.__duration} mins"