from movie import VideoRentalStore

store = VideoRentalStore()

store.add_movie("001", "Il Padrino", "Francis Ford Coppola")

store.register_customer("bo", "Mario Rossi")

store.rent_movie("bo", "001")


# Stampa film noleggiati da Mario
print("Film noleggiati da Mario Rossi:")
for film in store.get_rented_movies("bo"):
    print(f"{film.title} di {film.director}")


print("\nFilm noleggiati da Mario Rossi:")
for film in store.get_rented_movies("bo"):
    print(f"{film.title} di {film.director}")

store.return_movie("C001", "001")

print("\nFilm noleggiati da Mario Rossi dopo restituzione:")
for film in store.get_rented_movies("bo"):
    print(f"{film.title} di {film.director}")
