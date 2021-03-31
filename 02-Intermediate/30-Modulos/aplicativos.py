import calculos 

#print(calculos.PI)

#print(__name__) # nome dele é __main__

# 1)
# Em resumo, o arquivo que eu to executando primeiro é o __main__. Se eu tenho um modulo e executa-lo
# separadamente, ele também terá o nome __main__ . Porém, se eu importo esse módulo dentro de outro
# arquivo, este modulo passa a ter o nome do modulo em si e __main__ é o arquivo que to executando.

# Nesse caso, se for no arquivo calculos.py e executa-lo, print (__name__) que tem la vai imprimir __main__
# Porém, importando ele neste arquivo, este mesmo print que tem no calculos.py vai printar aqui
# o nome do modulo calculos e o comando abaixo vai imprimir __main__, pois o arquivo executado é este

lista = [10,20,30,40,50]

print(calculos.dobra_lista(lista))

