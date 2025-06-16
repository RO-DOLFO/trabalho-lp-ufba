'''
intercalar três listas: 

essa operação consistirá de quatro linhas: 
a primeira conterá apenas a letra ’j’;
a segunda, terceira e quarta linhas conterão, cada uma, uma lista de números inteiros. 

Essa operação é semelhante à operação intercala duas listas. No entanto, a intercalação será das três listas. 

Se as listas tiverem tamanhos diferentes, a intercalação deve continuar com as listas de maior tamanho até que todos os números tenham sido intercalados.
'''

def intercalar_tres_listas(l1,l2,l3):
    lista=[]

    if(len(l1) > len(l2)):
        n=len(l1)
    elif(len(l2) > len(l3)):
        n=len(l2)
    else:
        n=len(l3)


    for i in range(n):
        if(i < len(l1)):
            lista.append(l1[i])

        if(i < len(l2)):
            lista.append(l2[i])
        
        if(i < len(l3)):
            lista.append(l3[i])

#mostra a lista intercalada
    for item in lista:
        print(item, end=' ')