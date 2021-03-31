# Aplicação raiz do projeto.
# Packages é um diretório onde vou organizar meus módulos da mesma area do projeto. Para evitar escrever
# todas as minhas funções num módulo só, posso criar um diretório (no nosso caso vendas) e nele criar
# vários módulos com arquivos.py contendo códigos relaciondas a vendas.
# OBS: dentro do diretório package, sempre preciso ter o arquivo __init__.py, pois é quem informa
# para o inerpretador do python que este diretório é um package

import os
import sys
from vendas.calc_preco import aumento,reducao
from vendas.formata import preco as pco


preco = 49.90

#print(aumento(preco,15,formata=True))
preco_com_aumento = aumento(valor=preco,porcentagem=15,formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco,porcentagem=15,formata=True)
print(preco_com_aumento)

print(pco.real(59.95))


p = 50.50

p_aumento = aumento(valor=p,porcentagem=20,formata=True)
print(p)