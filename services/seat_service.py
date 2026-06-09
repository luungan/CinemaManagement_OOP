import json

from models.seat import StandardSeat, VIPSeat, CoupleSeat


class SeatService:
    def __init__(self):
        self.seat_list = []
        self.load_data()

    # Add seat
    def add_seat(self, seat):
        old_seat = self.find_seat_by_id(seat.seat_id)

        if old_seat is not None:
            print("Seat ID already exists")
            return False

        self.seat_list.append(seat)
        return True

    # Display seats
    def display_seats(self):
        if len(self.seat_list) == 0:
            print("Seat list is empty")
            return

        for seat in self.seat_list:
            print(seat)

    # Find seat
    def find_seat_by_id(self, seat_id):
        for seat in self.seat_list:
            if seat.seat_id == seat_id:
                return seat

        return None

    # Delete seat
    def delete_seat(self, seat_id):
        seat = self.find_seat_by_id(seat_id)

        if seat is not None:
            self.seat_list.remove(seat)
            return True

        return False

    # Book seat
    def book_seat(self, seat_id):
        seat = self.find_seat_by_id(seat_id)

        if seat is None:
            return False

        if seat.is_booked:
            print("Seat already booked")
            return False

        seat.is_booked = True
        return True

    # Save JSON
    def save_data(self):
        data = []

        for seat in self.seat_list:
            seat_type = type(seat).__name__

            seat_data = {
                "seat_id": seat.seat_id,
                "base_price": seat.base_price,
                "is_booked": seat.is_booked,
                "seat_type": seat_type
            }

            data.append(seat_data)

        with open("data/seats.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    
    # Load JSON
    def load_data(self):
        try:
            with open("data/seats.json", "r") as file:
                data = json.load(file)

                for item in data:
                    seat_type = item["seat_type"]

                    if seat_type == "StandardSeat":
                        seat = StandardSeat(
                            item["seat_id"],
                            item["base_price"]
                        )

                    elif seat_type == "VIPSeat":
                        seat = VIPSeat(
                            item["seat_id"],
                            item["base_price"]
                        )

                    else:
                        seat = CoupleSeat(
                            item["seat_id"],
                            item["base_price"]
                        )

                    seat.is_booked = item["is_booked"]

                    self.seat_list.append(seat)

        except:
            pass