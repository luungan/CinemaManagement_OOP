import csv

from models.movie import Movie
from models.showtime import Showtime
from models.seat import StandardSeat, VIPSeat, CoupleSeat
from models.ticket import Ticket

from services.movie_service import MovieService
from services.showtime_service import ShowtimeService
from services.seat_service import SeatService
from services.ticket_service import TicketService


movie_service = MovieService()
showtime_service = ShowtimeService()
seat_service = SeatService()
ticket_service = TicketService()


def menu():
    while True:
        print("\n===== CINEMA MANAGEMENT SYSTEM =====")
        print("1. Movie Management")
        print("2. Showtime Management")
        print("3. Seat Management")
        print("4. Ticket Booking")
        print("5. Reports")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            movie_menu()
        elif choice == "2":
            showtime_menu()
        elif choice == "3":
            seat_menu()
        elif choice == "4":
            ticket_menu()
        elif choice == "5":
            report_menu()
        elif choice == "0":
            movie_service.save_data()
            showtime_service.save_data()
            seat_service.save_data()
            ticket_service.save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def movie_menu():
    while True:
        print("\n--- MOVIE MANAGEMENT ---")
        print("1. Add Movie")
        print("2. Display Movies")
        print("3. Find Movie")
        print("4. Update Movie")
        print("5. Delete Movie")
        print("6. Sort By Title")
        print("7. Sort By Duration Desc")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                movie_id = input("Movie ID: ")
                title = input("Title: ")
                genre = input("Genre: ")
                duration = int(input("Duration: "))

                movie = Movie(movie_id, title, genre, duration)

                if movie_service.add_movie(movie):
                    movie_service.save_data()
                    print("Movie added successfully")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            movie_service.display_movies()

        elif choice == "3":
            movie_id = input("Enter movie ID: ")
            movie = movie_service.find_movie_by_id(movie_id)

            if movie is not None:
                print(movie)
            else:
                print("Movie not found")

        elif choice == "4":
            try:
                movie_id = input("Enter movie ID: ")
                new_title = input("New title: ")
                new_genre = input("New genre: ")
                new_duration = int(input("New duration: "))

                if movie_service.update_movie(movie_id, new_title, new_genre, new_duration):
                    movie_service.save_data()
                    print("Movie updated successfully")
                else:
                    print("Movie not found")
            except ValueError as e:
                print("Error:", e)

        elif choice == "5":
            movie_id = input("Enter movie ID: ")

            if movie_service.delete_movie(movie_id):
                movie_service.save_data()
                print("Movie deleted successfully")
            else:
                print("Movie not found")

        elif choice == "6":
            movie_service.sort_by_title()
            movie_service.display_movies()

        elif choice == "7":
            movie_service.sort_by_duration_desc()
            movie_service.display_movies()

        elif choice == "0":
            break

        else:
            print("Invalid choice")


def showtime_menu():
    while True:
        print("\n--- SHOWTIME MANAGEMENT ---")
        print("1. Add Showtime")
        print("2. Display Showtimes")
        print("3. Find Showtime")
        print("4. Update Showtime")
        print("5. Delete Showtime")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            showtime_id = input("Showtime ID: ")
            movie_title = input("Movie title: ")
            date = input("Date: ")
            time = input("Time: ")
            room = input("Room: ")

            showtime = Showtime(showtime_id, movie_title, date, time, room)

            if showtime_service.add_showtime(showtime):
                showtime_service.save_data()
                print("Showtime added successfully")

        elif choice == "2":
            showtime_service.display_showtimes()

        elif choice == "3":
            showtime_id = input("Enter showtime ID: ")
            showtime = showtime_service.find_showtime_by_id(showtime_id)

            if showtime is not None:
                print(showtime)
            else:
                print("Showtime not found")

        elif choice == "4":
            showtime_id = input("Enter showtime ID: ")
            new_movie_title = input("New movie title: ")
            new_date = input("New date: ")
            new_time = input("New time: ")
            new_room = input("New room: ")

            if showtime_service.update_showtime(
                showtime_id,
                new_movie_title,
                new_date,
                new_time,
                new_room
            ):
                showtime_service.save_data()
                print("Showtime updated successfully")
            else:
                print("Showtime not found")

        elif choice == "5":
            showtime_id = input("Enter showtime ID: ")

            if showtime_service.delete_showtime(showtime_id):
                showtime_service.save_data()
                print("Showtime deleted successfully")
            else:
                print("Showtime not found")

        elif choice == "0":
            break

        else:
            print("Invalid choice")


def seat_menu():
    while True:
        print("\n--- SEAT MANAGEMENT ---")
        print("1. Add Standard Seat")
        print("2. Add VIP Seat")
        print("3. Add Couple Seat")
        print("4. Display Seats")
        print("5. Delete Seat")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3"]:
            try:
                seat_id = input("Seat ID: ")
                base_price = float(input("Base price: "))

                if choice == "1":
                    seat = StandardSeat(seat_id, base_price)
                elif choice == "2":
                    seat = VIPSeat(seat_id, base_price)
                else:
                    seat = CoupleSeat(seat_id, base_price)

                if seat_service.add_seat(seat):
                    seat_service.save_data()
                    print("Seat added successfully")
            except ValueError as e:
                print("Error:", e)

        elif choice == "4":
            seat_service.display_seats()

        elif choice == "5":
            seat_id = input("Enter seat ID: ")

            if seat_service.delete_seat(seat_id):
                seat_service.save_data()
                print("Seat deleted successfully")
            else:
                print("Seat not found")

        elif choice == "0":
            break

        else:
            print("Invalid choice")


def ticket_menu():
    while True:
        print("\n--- TICKET BOOKING ---")
        print("1. Book Ticket")
        print("2. Display Tickets")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            ticket_id = input("Ticket ID: ")
            movie_title = input("Movie title: ")
            seat_id = input("Seat ID: ")

            seat = seat_service.find_seat_by_id(seat_id)

            if seat is None:
                print("Seat not found")
                continue

            if seat.is_booked:
                print("This seat is already booked")
                continue

            price = seat.calculate_price()
            ticket = Ticket(ticket_id, movie_title, seat_id, price)

            if ticket_service.add_ticket(ticket):
                seat_service.book_seat(seat_id)
                ticket_service.save_data()
                seat_service.save_data()
                print("Ticket booked successfully")
                print(ticket)

        elif choice == "2":
            ticket_service.display_tickets()

        elif choice == "0":
            break

        else:
            print("Invalid choice")


def report_menu():
    while True:
        print("\n--- REPORTS ---")
        print("1. Total Revenue")
        print("2. Total Tickets Sold")
        print("3. Total Movies")
        print("4. Total Showtimes")
        print("5. Available Seats")
        print("6. Export Report to CSV")
        print("0. Back")

        choice = input("Enter your choice: ")

        total_revenue = 0
        for ticket in ticket_service.ticket_list:
            total_revenue += ticket.price

        total_tickets = len(ticket_service.ticket_list)
        total_movies = len(movie_service.movie_list)
        total_showtimes = len(showtime_service.showtime_list)

        available_seats = 0
        for seat in seat_service.seat_list:
            if seat.is_booked == False:
                available_seats += 1

        if choice == "1":
            print(f"Total revenue: {total_revenue} VND")

        elif choice == "2":
            print(f"Total tickets sold: {total_tickets}")

        elif choice == "3":
            print(f"Total movies: {total_movies}")

        elif choice == "4":
            print(f"Total showtimes: {total_showtimes}")

        elif choice == "5":
            print(f"Available seats: {available_seats}")

        elif choice == "6":
            with open("data/report.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow(["Report", "Value"])
                writer.writerow(["Total Revenue", total_revenue])
                writer.writerow(["Total Tickets Sold", total_tickets])
                writer.writerow(["Total Movies", total_movies])
                writer.writerow(["Total Showtimes", total_showtimes])
                writer.writerow(["Available Seats", available_seats])

            print("Report exported successfully to data/report.csv")

        elif choice == "0":
            break

        else:
            print("Invalid choice")