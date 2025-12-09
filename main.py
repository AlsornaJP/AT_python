import pandas as pd
from scraping.get_soup import get_soup
from scraping.criar_dicionarios_filmes import criar_dicionarios_filmes

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
