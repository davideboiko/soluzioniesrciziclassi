class Movie:
    def __init__(self, movie_id: str, title: str, director: str):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
        else:
            print(f"Il film '{self.title}' è già noleggiato.")

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")


class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie: Movie):
        if movie.is_rented:
            print(f"Il film '{movie.title}' è già noleggiato")
        else:
            movie.rent()
            self.rented_movies.append(movie)

    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente")


class VideoRentalStore:
    def __init__(self):
        self.movies = {}      
        self.customers = {}   

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies:
            raise ValueError(f"Il film con ID '{movie_id}' esiste già.")
        self.movies[movie_id] = Movie(movie_id, title, director)

    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers:
            raise ValueError(f"Il cliente con ID '{customer_id}' è già registrato.")
        self.customers[customer_id] = Customer(customer_id, name)

    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)
        else:
            raise ValueError("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)
        else:
            raise ValueError("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            raise ValueError("Cliente non trovato.")
