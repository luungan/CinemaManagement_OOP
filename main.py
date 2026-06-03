from models.ticket import Ticket
from services.ticket_service import TicketService


service = TicketService()

ticket1 = Ticket("T01", "Avengers Endgame", "B01", 100000)

service.add_ticket(ticket1)

print("===== TICKET LIST =====")
service.display_tickets()

service.save_data()
