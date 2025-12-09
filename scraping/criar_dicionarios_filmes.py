from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def criar_dicionarios_filmes(html):

    filmes = html.find_all("li", class_="ipc-metadata-list-summary-item")
    lista_de_dicionarios_filme = []
    for filme in filmes:
        titulo = filme.find("h3", class_="ipc-title__text")
        ano = filme.find("span", class_="sc-b4f120f6-7 hoOxkw cli-title-metadata-item")
        nota = filme.find("span", class_="ipc-rating-star--rating")

        filme_dict = {
            "Titulo":titulo.get_text(strip=True),
            "Ano":ano.get_text(strip=True),
            "Nota":nota.get_text(strip=True)
        }
        lista_de_dicionarios_filme.append(filme_dict)
    return lista_de_dicionarios_filme

