class Showtime:
    def __init__(self, showtime_id, moive_title, date, time, room):
        self.__showtime_id = showtime_id
        self.__movie_title = moive_title
        self.__date = date
        self.__time = time
        self.__room = room
    @property
    def showtime_id(self):
        return self.__showtime_id

    @property
    def movie_title(self):
        return self.__movie_title

    @movie_title.setter
    def movie_title(self, value):
        self.__movie_title = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        self.__room = value

    def to_dict(self):
        return {
            "showtime_id": self.__showtime_id,
            "movie_title": self.__movie_title,
            "date": self.__date,
            "time": self.__time,
            "room": self.__room
        }

    def __str__(self):
        return f"{self.__showtime_id} | {self.__movie_title} | {self.__date} | {self.__time} | Room {self.__room}"    