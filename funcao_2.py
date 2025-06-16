'''
pares antes de ímpares em ordem crescente:

#entrada
essa operação consistirá de duas linhas: aprimeira conterá apenas a letra ’o’; 
a segunda conterá uma lista de números inteiros.

#saida
Essa operação é semelhante à operação anterior, com a diferença de que os números pares e os
números ímpares devem estar em ordem crescente, considerando separadamente cada um dos
tipos de números. Ou seja, os pares devem estar ordenados e, em seguida, os ímpares ordenados.
'''
def pares_antes_de_impares_em_ordem_crescente(lista):

    lista_par=[]
    soma_par=0
    media_par=0

    lista_imp=[]
    soma_imp=0
    media_imp=0

#varre a lista para separar os pares dos impares.
    for i in range(len(lista)):
        if(lista[i] % 2 == 0):
            lista_par.append(lista[i])
        else:
            lista_imp.append(lista[i])
    
    lista_par.sort()
    lista_imp.sort()

#mostra a lista separada pares e impares
    for i in range(len(lista_par)):
        print(lista_par[i], end=' ')

    for i in range(len(lista_imp)):
        print(lista_imp[i], end=' ')
