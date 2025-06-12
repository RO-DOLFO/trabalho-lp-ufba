'''
2 Formato da Entrada e Saída

A entrada consistirá de uma sequência com um número arbitrário de operações. 
O programa deve ler as operações e executá-las (gerar suas saídas). 
A última operação é a de término de sequência
(indicada abaixo).
Todas as sequências conterão apenas números inteiros.
As operações e seus formatos são:
'''
'''
1. pares antes de ímpares na ordem em que aparecem:
essa operação consistirá de duas linhas:
    a primeira conterá apenas a letra ’a’; 
    a segunda conterá uma lista de números inteiros.

Essa operação imprime na saída os números pares e, em seguida, os ímpares. 
Os números pares e ímpares devem aparecer na ordem relativa em que aparecem na lista original. 
Os números devem ser separados por um espaço.

Na linha seguinte, o programa deve gerar na saída a sequência "media dos pares:", seguida por um espaço, seguido do valor da média dos números pares, com uma casa decimal.

Na terceira linha, o programa deve gerar na saída a sequência "media dos impares:", seguida por um espaço, seguido do valor da média dos números ímpares, com uma casa decimal.
'''

def pares_antes_de_impares(lista):

    lista_par=[]
    soma_par=0
    media_par=0

    lista_imp=[]
    soma_imp=0
    media_imp=0

    print('a')

#varre a lista para separar os pares dos impares.
    for i in range(len(lista)):
        if(lista[i] % 2 == 0):
            lista_par.append(lista[i])
        else:
            lista_imp.append(lista[i])

#mostra a lista separada pares e impares
    for i in range(len(lista_par)):
        print(lista_par[i], end=' ')

    for i in range(len(lista_imp)):
        print(lista_imp[i], end=' ')

    print('')

    for i in range(len(lista_par)):
        soma_par += lista_par[i]

    for i in range(len(lista_imp)):
        soma_imp += lista_imp[i]


#testa se a lista é 0 pq não da para dividir por 0
#constroi a media dos pares e impares
    if(len(lista_par) > 0):
        media_par = soma_par / len(lista_par)
        print(f'Media dos pares: {media_par:.1f}')
    else:
        print(f'Media dos pares: 0.0')


    if(len(lista_imp) > 0):
        media_imp = soma_imp / len(lista_imp)
        print(f'Media dos impares: {media_imp:.1f}')
    else:
        print(f'Media dos impares: 0.0')


l=[1,2,3,4,5]

pares_antes_de_impares(l)


