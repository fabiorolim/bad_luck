import random

import requests
from bs4 import BeautifulSoup

URL_MODULO_1 = "https://fabiorolim.github.io/test_scrap/"

page = requests.get(URL_MODULO_1)
soup = BeautifulSoup(page.content, 'html.parser')
lista = soup.find_all('a', title="Consulta Dados do Aluno")
nomes = []
sorteados = []

for l in lista:
    if str(l.get_text()).startswith('2'):
        pass
    else:
        nomes.append(str(l.get_text()).replace("\n", "").replace(" " * 33, ""))


def sortear():
    while len(nomes) > len(sorteados):
        sorteado = nomes[random.randint(0, len(nomes) - 1)]
        if sorteado not in sorteados:
            sorteados.append(sorteado)


def exibir_sorteados():
    i = 1
    for nome in sorteados:
        print(f'{i} - {nome}')
        i += 1


sortear()
exibir_sorteados()
