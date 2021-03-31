# Resumo: arquivos.py que contem codigo python em que posso exportar pra dentro do nosso código e estender a funcionalidade da linguagem
# import, from e as - palavras principais

import sys

print(sys.platform)

# importar apenas o que eu quero usar. Posso usuar agora so "plataform" ao inves de "sys.plataform"

from sys import platform

print(sys.platform)

from os import listdir # CRTL + SPACE -> listo todos os recursos do modulo!!!!

teste = listdir()
print(listdir())

from os import listdir as ls # alias

print(ls())

import random

print(random.randint(0,10)) # Gera aleatório entre 0 e 10

# IMPORTAR MAIS DE UM NA MESMA LINHA

from random import randint, random # posso importar tudo from random import * , não é uma boa prática para debug principalmente.

print(randint(0,10),random())