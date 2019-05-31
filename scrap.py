import random
import requests
from bs4 import BeautifulSoup


class Scrap:

    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)

    def get_soup(self):
        return BeautifulSoup(self.page.content, 'html.parser')

    def get_results(self, soup):
        return soup.find_all('a', title="Consulta Dados do Aluno")

    @classmethod
    def get_nomes(cls, lista):
        nomes = []
        for l in lista:
            if str(l.get_text()).startswith('2'):
                pass
            else:
                nomes.append(
                    # str(l.get_text()).replace("\n", "").replace(" " * 33, ""))
                    str(l.get_text()).replace("\n", "").replace(" " * 15, ""))
        return nomes


class Sorteio:

    def __init__(self, nomes):
        self.nomes = nomes
        self.sorteados = []

    def luck(self):
        while len(self.nomes) > len(self.sorteados):
            self.sorteado = self.nomes[random.randint(0, len(self.nomes) - 1)]
            if self.sorteado not in self.sorteados:
                self.sorteados.append(self.sorteado)
        return self.sorteados

    def show_names(self):
        i = 1
        for sorteado in self.sorteados:
            print(f'{i} - {sorteado}')
            i += 1
