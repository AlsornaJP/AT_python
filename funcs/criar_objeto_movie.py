from classes.Movie import Movie

def criar_objeto_movie(dicionario):

    filme = Movie(
        title = dicionario['titulo'],
        year = dicionario['ano'],
        rating = dicionario['nota']
    )

    return filme