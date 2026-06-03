class Ticket:
    def __init__(self, ticket_id, movie_title, seat_id, price):
        self.__ticket_id = ticket_id
        self.__movie_title = movie_title
        self.__seat_id = seat_id
        self.__price = price

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def movie_title(self):
        return self.__movie_title

    @property
    def seat_id(self):
        return self.__seat_id

    @property
    def price(self):
        return self.__price

    def to_dict(self):
        return {
            "ticket_id": self.__ticket_id,
            "movie_title": self.__movie_title,
            "seat_id": self.__seat_id,
            "price": self.__price
        }

    def __str__(self):
        return f"{self.__ticket_id} | {self.__movie_title} | Seat {self.__seat_id} | {self.__price} VND"