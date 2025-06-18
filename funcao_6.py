def ordena_por_frequencia_de_ocorrencia(l1):

    dicionario = {}

    for numero in l1:
        if numero in dicionario:
            dicionario[numero] += 1
        else:
            dicionario[numero] = 1

    # Transforma em listas para ordenar
    numeros = list(dicionario.keys())
    frequencias = list(dicionario.values())

    # Ordenação manual (bolha) por frequência e depois por valor
    n = len(numeros)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Se a frequência atual é maior que a próxima, troca
            if frequencias[j] > frequencias[j + 1]:
                frequencias[j], frequencias[j + 1] = frequencias[j + 1], frequencias[j]
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            # Se frequência for igual, ordena pelo número menor
            elif frequencias[j] == frequencias[j + 1] and numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

    # Impressão no formato pedido
    for i in range(n):
        print(f"{numeros[i]} ({frequencias[i]})", end=' ')
    print("")