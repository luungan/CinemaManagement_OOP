from models.movie import Movie
from services.movie_service import MovieService


service = MovieService()


def menu():
    while True:
        print("\n===== CINEMA MANAGEMENT SYSTEM =====")
        print("1. Add Movie")
        print("2. Display Movies")
        print("3. Find Movie")
        print("4. Update Movie")
        print("5. Delete Movie")
        print("6. Sort By Title")
        print("7. Sort By Duration Desc")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            movie_id = input("Enter movie ID: ")
            title = input("Enter title: ")
            genre = input("Enter genre: ")

            try:
                duration = int(input("Enter duration: "))

                movie = Movie(movie_id, title, genre, duration)
                result = service.add_movie(movie)

                if result:
                    print("Add successfully")

            except ValueError:
                print("Duration must be a number and greater than 0")

        elif choice == "2":
            service.display_movies()

        elif choice == "3":
            movie_id = input("Enter movie ID: ")
            movie = service.find_movie_by_id(movie_id)

            if movie is not None:
                print(movie)
            else:
                print("Movie not found")

        elif choice == "4":
            movie_id = input("Enter movie ID: ")
            new_title = input("Enter new title: ")
            new_genre = input("Enter new genre: ")

            try:
                new_duration = int(input("Enter new duration: "))

                result = service.update_movie(
                    movie_id,
                    new_title,
                    new_genre,
                    new_duration
                )

                if result:
                    print("Update successfully")
                else:
                    print("Movie not found")

            except ValueError:
                print("Duration must be a number and greater than 0")

        elif choice == "5":
            movie_id = input("Enter movie ID: ")
            result = service.delete_movie(movie_id)

            if result:
                print("Delete successfully")
            else:
                print("Movie not found")

        elif choice == "6":
            service.sort_by_title()
            service.display_movies()

        elif choice == "7":
            service.sort_by_duration_desc()
            service.display_movies()

        elif choice == "0":
            service.save_data()
            print("Exit program")
            break

        else:
            print("Invalid choice")