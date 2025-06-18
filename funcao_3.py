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