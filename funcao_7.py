def pares_antes_de_impares_ordena_dentro_da_categoria_e_intercala(l1, l2):
    lista_par_1 = []
    lista_imp_1 = []

    for i in range(len(l1)):
        if l1[i] % 2 == 0:
            lista_par_1.append(l1[i])
        else:
            lista_imp_1.append(l1[i])

    # Separação dos pares e ímpares da segunda lista
    lista_par_2 = []
    lista_imp_2 = []

    for i in range(len(l2)):
        if l2[i] % 2 == 0:
            lista_par_2.append(l2[i])
        else:
            lista_imp_2.append(l2[i])

    # Ordenando as listas de pares e ímpares da primeira lista
    lista_par_1.sort()
    lista_imp_1.sort()

    # Ordenando as listas de pares e ímpares da segunda lista
    lista_par_2.sort()
    lista_imp_2.sort()

    # Intercalando os pares
    lista_intercalada_par = []

    tamanho_par_1 = len(lista_par_1)
    tamanho_par_2 = len(lista_par_2)

    max_par = tamanho_par_1
    if tamanho_par_2 > max_par:
        max_par = tamanho_par_2

    for i in range(max_par):
        if i < tamanho_par_1:
            lista_intercalada_par.append(lista_par_1[i])
        if i < tamanho_par_2:
            lista_intercalada_par.append(lista_par_2[i])

    # Intercalando os ímpares
    lista_intercalada_imp = []

    tamanho_imp_1 = len(lista_imp_1)
    tamanho_imp_2 = len(lista_imp_2)

    max_imp = tamanho_imp_1
    if tamanho_imp_2 > max_imp:
        max_imp = tamanho_imp_2

    for i in range(max_imp):
        if i < tamanho_imp_1:
            lista_intercalada_imp.append(lista_imp_1[i])
        if i < tamanho_imp_2:
            lista_intercalada_imp.append(lista_imp_2[i])

    # Juntando os pares e ímpares
    lista_final = []

    for i in range(len(lista_intercalada_par)):
        lista_final.append(lista_intercalada_par[i])

    for i in range(len(lista_intercalada_imp)):
        lista_final.append(lista_intercalada_imp[i])

    for item in lista_final:
        print(item, end=' ')
    print()
