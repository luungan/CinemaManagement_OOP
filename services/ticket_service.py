import json

from models.ticket import Ticket


class TicketService:
    def __init__(self):
        self.ticket_list = []
        self.load_data()

    def add_ticket(self, ticket):
        old_ticket = self.find_ticket_by_id(ticket.ticket_id)

        if old_ticket is not None:
            print("Ticket ID already exists")
            return False

        self.ticket_list.append(ticket)
        return True

    def display_tickets(self):
        if len(self.ticket_list) == 0:
            print("Ticket list is empty")
            return

        for ticket in self.ticket_list:
            print(ticket)

    def find_ticket_by_id(self, ticket_id):
        for ticket in self.ticket_list:
            if ticket.ticket_id == ticket_id:
                return ticket

        return None

    def save_data(self):
        data = []

        for ticket in self.ticket_list:
            data.append(ticket.to_dict())

        with open("data/tickets.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("data/tickets.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                for item in data:
                    ticket = Ticket(
                        item["ticket_id"],
                        item["movie_title"],
                        item["seat_id"],
                        item["price"]
                    )

                    self.ticket_list.append(ticket)

        except:
            pass