import pandas as pd
from scraping.get_soup import get_soup
from scraping.criar_dicionarios_filmes import criar_dicionarios_filmes
from funcs.criar_objeto_movie import criar_objeto_movie
from classes.Series import Series
from classes.Movie import Movie
from banco_de_dados.tabelas import Session,movies,series, engine
from banco_de_dados.adicionar_registros import adicionar_entradas
from funcs.adaptar_nota import adaptar_nota
import json
import csv



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
print(df_filmes)
print('\n')

# criando lista de objetos movie
objetos_movie = []
for filme in lista_de_filmes:
    objetos_movie.append(criar_objeto_movie(filme))

series_aleatorias = [Series(title='Breaking Bad', year='2008', seasons='5', episodes='62'), Series(title='Ruptura', year='2022', seasons='2', episodes='19')]
objetos_movie.extend(series_aleatorias)
[print(filme) for filme in objetos_movie]
print('\n')


# adicionando registros nas tabelas

'''adicionar_entradas(objetos_movie)'''

# transformando tabelas em dataframes
tabela_movies_inteira = None
with Session() as session:
    tabela_movies_inteira = session.query(movies).all()

df_movies = pd.DataFrame([objeto.__dict__ for objeto in tabela_movies_inteira]).drop('_sa_instance_state',axis=1)
df_movies.set_index('movie_id',inplace=True)
print(df_movies[:5])
print('\n')


tabela_series_inteira = None
with Session() as session:
    tabela_series_inteira = session.query(series).all()

df_series = pd.DataFrame([objeto.__dict__ for objeto in tabela_series_inteira]).drop('_sa_instance_state',axis=1)
df_series.set_index('series_id',inplace=True)
print(df_series[:5])
print('\n')


# exportando dados

df_movies_ordenado = df_movies[df_movies['rating'] > 9.0].sort_values('rating', ascending=False)
print(df_movies_ordenado[0:5])
print('\n')


conteudo_movies = df_movies.to_json()
csv_movies = df_movies.to_csv()
conteudo_series = df_series.to_json()
csv_series = df_series.to_csv()

'''with open("movies.json","w",encoding="utf-8") as arquivo:
    arquivo.write(conteudo_movies)
with open("movies.csv","w",encoding="utf-8") as arquivo:
    arquivo.write(csv_movies)

with open("series.json","w",encoding="utf-8") as arquivo:
    arquivo.write(conteudo_series)
with open("series.csv","w",encoding="utf-8") as arquivo:
    arquivo.write(csv_series)'''

# criação de coluna categoria

df_movies['categoria'] = df_movies['rating'].apply(adaptar_nota)
print(df_movies[:10])
print('\n')


# tabela filmes por ano

contagem_filmes_por_ano = df_movies.groupby('year')['title'].count()
print(contagem_filmes_por_ano.sort_values(ascending=False))
'''contagem_filmes_por_ano.to_sql('filmes_ano', engine)'''

