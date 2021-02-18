import os
from domain.Movie import Movie

class MovieService :

    @staticmethod
    def add_movie_catalogo(name_movie) :
        movie = Movie(name_movie)
        file = open("catalogo.txt", "w")
        file.write(f"{ movie.get_name_movie() }\n")

    @staticmethod
    def list_movie_catalogo() :
        file = open("catalogo.txt", "r")
        for line_movie in file :
            print(f"{line_movie}\n")
        

    @staticmethod
    def delete_catalogo() :
        try :
            os.remove("catalogo.txt")
        except OSError as error :
            print("Ha ocurrido un erro: ", error)


