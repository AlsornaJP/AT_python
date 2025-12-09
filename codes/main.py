from get_soup import get_soup
import pandas as pd

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

print(dez_primeiros_filmes)
