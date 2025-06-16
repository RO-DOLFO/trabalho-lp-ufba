'''
intercala duas listas: 
essa operação consistirá de três linhas:

#ENTRADA
a primeira conterá apenas a letra ’i’; 
a segunda e a terceira conterão, cada uma, uma lista de números inteiros.

#SAIDA
Essa operação gera, na saída, a intercalação entre as duas listas, ou seja, o primeiro caractere da
primeira lista, seguido do primeiro caractere da segunda lista, seguido do segundo caractere da
primeira lista, seguido pelo segundo caractere da segunda lista e assim por diante.

As listas podem ter tamanhos diferentes. Se isso acontecer, os números restantes da lista maior
devem aparecer ao final da lista intercalada.

Os números da lista devem ser separados por um espaço.
Em seguida, a operação deve gerar, em uma nova linha, a sequência "maior valor:", seguido de
um espaço, seguido do maior valor da lista intercalada final.
1
Em uma terceira linha, a operação deve gerar a sequência "quantidade de pares:", seguido de um
espaço, seguido do número de pares na lista intercalada final.

Em uma quarta linha, a operação deve gerar a sequência "quantidade de impares:", seguido de
um espaço, seguido do número de ímpares na lista intercalada final.'''

def intercala_duas_listas(l1,l2):
    lista=[]
    cont_par=0
    cont_imp=0

    if(len(l1) > len(l2)):
        n=len(l1)
    else:
        n=len(l2)

    for i in range(n):
        if(i < len(l1)):
            lista.append(l1[i])

        if(i < len(l2)):
            lista.append(l2[i])

#mostra a lista intercalada
    for item in lista:
        print(item, end=' ')

# contar os pares e impares
    for item in lista:
        if(item % 2 == 0):
            cont_par+=1
        else:
            cont_imp+=1
    
    
    print()
    if(len(lista) > 0):
        print(f'maior valor: {max(lista)}')
    else:
        print(f'maior valor: ')

    print(f'quantidade de pares: {cont_par}')
    print(f'quantidade de impares: {cont_imp}')