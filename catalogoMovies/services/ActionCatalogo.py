class MovieService :

    @staticmethod
    def add_movie_catalogo(name_movie) :
        file = open("catalogo.txt", "w")
        file.write(f"{name_movie}\n")

    @staticmethod
    def list_movie_catalogo() :
        pass

    @staticmethod
    def delete_catalogo() :
        pass


