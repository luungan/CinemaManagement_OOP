from abc import ABC, abstractmethod


class Seat(ABC):
    def __init__(self, seat_id, base_price):
        self.__seat_id = seat_id
        self.__base_price = base_price
        self.__is_booked = False

    @property
    def seat_id(self):
        return self.__seat_id

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            raise ValueError("Base price cannot be negative")
        self.__base_price = value

    @property
    def is_booked(self):
        return self.__is_booked

    @is_booked.setter
    def is_booked(self, value):
        self.__is_booked = value

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def get_seat_type(self):
        pass

    def __str__(self):
        status = "Booked" if self.__is_booked else "Available"
        return f"{self.__seat_id} | {self.get_seat_type()} | {self.calculate_price()} VND | {status}"


class StandardSeat(Seat):
    def calculate_price(self):
        return self.base_price

    def get_seat_type(self):
        return "Standard"


class VIPSeat(Seat):
    def calculate_price(self):
        return self.base_price + 30000

    def get_seat_type(self):
        return "VIP"


class CoupleSeat(Seat):
    def calculate_price(self):
        return self.base_price * 2

    def get_seat_type(self):
        return "Couple"