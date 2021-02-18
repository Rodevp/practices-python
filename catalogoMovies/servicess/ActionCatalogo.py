import os
from domain.Movie import Movie

class MovieService :

    @staticmethod
    def add_movie_catalogo(name_movie) :
        try :
            movie = Movie(name_movie)
            file = open("catalogo.txt", "w")
            file.write(f"{ movie.get_name_movie() }\n")
        except OSError as error :
            print("Upas, un error 💀")


    @staticmethod
    def list_movie_catalogo() :
        try :
            file = open("catalogo.txt", "r")
            for line_movie in file :
                print(f"{line_movie}\n")
        except OSError as error :
            print("Upss, no tienes pelis 👀")
            

    @staticmethod
    def delete_catalogo() :
        try :
            os.remove("catalogo.txt")
        except OSError as error :
            print("Ha ocurrido un erro: ", error)


