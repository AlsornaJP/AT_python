from classes.movie import movie

def criar_objeto_movie(dicionario):

    filme = movie(
        title = dicionario['titulo'],
        year = dicionario['ano'],
        rating = dicionario['nota']
    )

    return filme