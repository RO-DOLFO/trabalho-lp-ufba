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

    print('')

    for i in range(len(lista_par)):
        soma_par += lista_par[i]

    for i in range(len(lista_imp)):
        soma_imp += lista_imp[i]


#testa se a lista é 0 pq não da para dividir por 0
#constroi a media dos pares e impares
    if(len(lista_par) > 0):
        media_par = soma_par / len(lista_par)
        print(f'media dos pares: {media_par:.1f}')
    else:
        print(f'media dos pares: 0.0')

    if(len(lista_imp) > 0):
        media_imp = soma_imp / len(lista_imp)
        print(f'media dos impares: {media_imp:.1f}')
    else:
        print(f'media dos impares: 0.0')