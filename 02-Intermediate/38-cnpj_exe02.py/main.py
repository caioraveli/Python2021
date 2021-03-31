from cnpj import cnpj
from cnpj import gerador_cnpj
import re

new_cnpj = gerador_cnpj.gera()
new_cnpj2 = cnpj.refaz_cnpj(new_cnpj)
print(type(new_cnpj2))
print(cnpj.valida(new_cnpj2))
