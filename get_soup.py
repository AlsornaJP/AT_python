from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_soup(link):
    """
    Recebe um link formato string e retorna um objeto da classe bs4
    """
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
    req = Request(url=link, headers=headers)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup