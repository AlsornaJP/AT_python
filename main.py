from get_soup import get_soup
import pandas as pd


url_imdb = "https://www.imdb.com/pt/chart/top/"
html_imdb = get_soup(url_imdb)

dez_primeiros_filmes = []

