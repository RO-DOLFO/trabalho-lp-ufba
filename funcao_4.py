'''
intercala sem repetição: 
#ENTRADA
essa operação consistirá de três linhas: 
a primeira conterá apenas a letra ’s’; 
a segunda e a terceira conterão, cada uma, uma lista de números inteiros.

Essa operação é semelhante à operação anterior, mas, na lista intercalada final, não pode haver números repetidos. Ou seja, se um número ocorrer mais do que uma vez, considerando as duas listas juntas, ele deve aparecer apenas uma vez na lista final. 

A primeira ocorrência de cada número repetido é a que deve aparecer na lista final.
'''

def intercala_sem_repeticao(l1,l2):
    lista=[]
    lista_sem_rep=[]

    if(len(l1) > len(l2)):
        n=len(l1)
    else:
        n=len(l2)

    for i in range(n):
        if(i < len(l1)):
            lista.append(l1[i])

        if(i < len(l2)):
            lista.append(l2[i])

#tira as repeticoes
    for item in lista:
        if(item not in lista_sem_rep):
            lista_sem_rep.append(item)
    
#mostra a lista intercalada
    for item in lista_sem_rep:
        print(item, end=' ')

