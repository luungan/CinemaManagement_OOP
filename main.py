from services.movie_service import MovieService


service = MovieService()

print("===== MOVIE LIST =====")
service.display_movies()

print("\n===== UPDATE MOVIE =====")

result = service.update_movie(
    "M01",
    "Avengers Endgame",
    "Action",
    200
)

if result:
    print("Update successfully")
else:
    print("Movie not found")

print("\n===== MOVIE LIST AFTER UPDATE =====")
service.display_movies()

service.save_data()