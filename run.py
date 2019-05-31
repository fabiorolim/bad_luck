# TODO: Scrap direito do qacademico :)

import sys
from scrap import Scrap, Sorteio

URL_MODULO_1 = "https://fabiorolim.github.io/bad_luck/modulo1/"
URL_MODULO_3 = "https://fabiorolim.github.io/bad_luck/modulo3/"

print('#' * 30)
print('##     1 - Módulo 1        ##')
print('##     3 - Módulo 3        ##')
print('##     0 - Sair            ##')
print('#' * 30)

op = input("Informe a opção: ")

if op == '1':
    url = URL_MODULO_1
elif op == '3':
    url = URL_MODULO_3
else:
    sys.exit()

scrap = Scrap(url)
results_soap = scrap.get_results(scrap.get_soup())
nomes = scrap.get_nomes(results_soap)
sorteio = Sorteio(nomes)
sorteados = sorteio.luck()
sorteio.show_names()
