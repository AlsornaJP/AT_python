import pandas as pd
from scraping.get_soup import get_soup
from scraping.criar_dicionarios_filmes import criar_dicionarios_filmes
from funcs.criar_objeto_movie import criar_objeto_movie
from classes.series import series

# HTML inicial
url_imdb = "https://www.imdb.com/pt/chart/top/"
html_imdb = get_soup(url_imdb)

# coletando os 10 primeiros títulos
lista_titulos_filmes = html_imdb.find_all("h3", class_="ipc-title__text")
dez_primeiros_filmes = []
contador_de_filmes = 1

while contador_de_filmes < 10:
    for filme in lista_titulos_filmes:
        if contador_de_filmes > 10:
            break
        dez_primeiros_filmes.append(filme.get_text(strip=True))
        contador_de_filmes +=1

print(f"\nLista dos 10 primeiros filmes: {dez_primeiros_filmes}\n")

# coletando intformações sobre filmes

lista_de_filmes = criar_dicionarios_filmes(html_imdb)
df_filmes = pd.DataFrame(lista_de_filmes)
df_filmes

# criando lista de objetos movie
objetos_movie = []
for filme in lista_de_filmes:
    objetos_movie.append(criar_objeto_movie(filme))

series_aleatorias = [series(title='Breaking Bad', year='2008', seasons='5', episodes='62'), series(title='Ruptura', year='2022', seasons='2', episodes='19')]
objetos_movie.extend(series_aleatorias)
[print(filme) for filme in objetos_movie]