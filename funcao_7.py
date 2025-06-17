'''
pares antes de ímpares, ordena dentro da categoria e intercala:

#entrada
essa operação consistirá de três linhas: 
a primeira conterá apenas a letra ’m’; 
a segunda e a terceira conterão, cada uma, uma lista de números inteiros.

#saida
Essa operação gera, na saída, uma lista final que consiste do resultado das seguintes operações:
    colocar os números pares antes dos ímpares em cada uma das listas;

    ordenar separadamente os pares e ímpares, de cada uma das duas listas;

    intercalar os números pares das duas listas;
    intercalar os números ímpares das duas listas.
'''

def pares_antes_de_impares_ordena_dentro_da_categoria_e_intercala(l1, l2):

    lista_par_1=[]
    lista_imp_1=[]
    
    lista_par_2=[]
    lista_imp_2=[]

    lista_intercalada_par=[]
    lista_intercalada_imp=[]

# estrutura para l1
#varre a lista para separar os pares dos impares.
    for i in range(len(l1)):
        if(l1[i] % 2 == 0):
            lista_par_1.append(l1[i])
        else:
            lista_imp_1.append(l1[i])

#mostra a lista separada pares e impares
    for item in lista_par_1:
        print(item, end=' ')

    for item in lista_imp_1:
        print(item, end=' ')

    print('')

# estrutura para l2
#varre a lista para separar os pares dos impares.
    for i in range(len(l2)):
        if(l2[i] % 2 == 0):
            lista_par_2.append(l2[i])
        else:
            lista_imp_2.append(l2[i])

#mostra a lista separada pares e impares
    for item in lista_par_2:
        print(item, end=' ')

    for item in lista_imp_2:
        print(item, end=' ')

#Ordena as listas
    lista_par_1.sort()
    lista_imp_1.sort()

    lista_par_2.sort()
    lista_imp_2.sort()

    print()

#mostra a lista com os pares separdos dos impares e ordenados
    for item in lista_par_1:
        print(item, end=' ')
    for item in lista_imp_1:    
        print(item, end=' ')
    
    for item in lista_par_2:
        print(item, end=' ')
    for item in lista_imp_2:
        print(item, end=' ')

    print()

# alimenta a lista intercalada de pares
    if(len(lista_par_1) > len(lista_par_2)):
        n = len(lista_par_1)
    else:
        n = len(lista_par_2)

    for i in range(n):
        if(i < len(lista_par_1)):
            lista_intercalada_par.append(lista_par_1[i])

        if(i < len(lista_par_2)):
            lista_intercalada_par.append(lista_par_2[i])

#mostra a lista intercalada
    for item in lista_intercalada_par:
        print(item, end=' ')
    
    print()

# alimenta a lista intercalada de impares
    if(len(lista_imp_1) > len(lista_imp_2)):
        n = len(lista_imp_1)
    else:
        n = len(lista_imp_2)

    for i in range(n):
        if(i < len(lista_imp_1)):
            lista_intercalada_imp.append(lista_imp_1[i])

        if(i < len(lista_imp_2)):
            lista_intercalada_imp.append(lista_imp_2[i])

#mostra a lista intercalada
    for item in lista_intercalada_imp:
        print(item, end=' ')
