'''
ordena por frequência de ocorrência:

#entrada
essa operação consistirá de duas linhas: 
a primeira conterá apenas a letra ’f’; 
a segunda conterá uma lista de números inteiros. 

#saida
Essa operação gera, na saída, os números por ordem crescente de frequência de ocorrência.
Os números que ocorrerem mais de uma vez devem aparecer uma única vez na saída.

Após cada número deve aparecer um espaço, seguido da quantidade de vezes em que ocorre, entre parênteses. 

Por exemplo, suponha que o número 4 ocorra cinco vezes na lista e o número 10, uma vez. A saída deve ser: 10 (1) 4 (5). Os números com mesma frequência de ocorrência devem aparecer em ordem crescente.
'''

def ordena_por_frequencia_de_ocorrencia(l1):
    lista_sem_rep=[]
    cont=0

    for i in range(len(l1)):
        if(l1[i] == l1[i]+1):
            cont+=1

# tira as repetições 
    for item in l1:
        if(item not in lista_sem_rep):
            lista_sem_rep.append(item)

# mostra a lista sem repetições
    for i in lista_sem_rep:
        print(i, end=' ')

    print('')
#lista full
    for i in range(len(l1)):
        print(l1[i], end=' ')


#teste
