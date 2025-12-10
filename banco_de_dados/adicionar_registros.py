from banco_de_dados.tabelas import Session, movies, series
from classes.Movie import Movie
from classes.Series import Series



def adicionar_entradas(lista_de_objetos):
    with Session() as session:
        for objeto in lista_de_objetos:
            tipo = type(objeto)
            filme = None
            
            if tipo.__name__ == 'Movie':
                filme = movies(
                    title = objeto.title,
                    year = objeto.year,
                    rating = float(objeto.rating.replace(',','.'))
                )
                session.add(filme)

            elif tipo.__name__ == 'Series':
                filme = series(
                    title = objeto.title,
                    year = objeto.year,
                    seasons = int(objeto.seasons),
                    episodes = int(objeto.episodes)
                )
                session.add(filme)
        session.commit()
