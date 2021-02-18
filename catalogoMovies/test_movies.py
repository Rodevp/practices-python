from servicess.ActionCatalogo import MovieService

class  Main :
    __template = """
        ----Catalogo De Peliculas🖥----\n
        - Elige tu opcion:\n
        1. Agregar Pelicula\n
        2. Listar peliculas\n
        3. Eliminar catalogo\n
        4. Salir\n 
    """

    def __init__(self) -> None:
        self.main()

    def main(self) :
        while True :
            option = input(self.__template)
            if option == "1" :
                name_movie = input("Nombre de pelicula: ")
                MovieService.add_movie_catalogo(name_movie)
            if option == "2" :
                MovieService.list_movie_catalogo()
            if option == "3" :
                MovieService.delete_catalogo()
            if option == "4" :
                print("Bye ✌")
                break


app = Main()