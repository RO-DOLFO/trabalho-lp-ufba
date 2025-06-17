from funcoes.funcao_1 import pares_antes_de_impares
from funcoes.funcao_2 import pares_antes_de_impares_em_ordem_crescente
from funcoes.funcao_3 import intercala_duas_listas
from funcoes.funcao_4 import intercala_sem_repeticao
from funcoes.funcao_5 import intercalar_tres_listas
from funcoes.funcao_6 import ordena_por_frequencia_de_ocorrencia
from funcoes.funcao_7 import pares_antes_de_impares_ordena_dentro_da_categoria_e_intercala

var = input()

#questão 1
if(var == 'a'):
    lista = input()
    lista = lista.split()
    lista_de_numeros = []

    for item in lista:
        numero = int(item)
        lista_de_numeros.append(numero)

    pares_antes_de_impares(lista_de_numeros)

#questão 2
if(var == 'o'):
    lista = input()
    lista = lista.split()
    lista_de_numeros = []

    for item in lista:
        numero = int(item)
        lista_de_numeros.append(numero)

    pares_antes_de_impares_em_ordem_crescente(lista_de_numeros)

#questão 3
if(var == 'i'):
    lista1 = input()
    lista1 = lista1.split()
    lista1_de_numeros = []

    for item in lista1:
        numero = int(item)
        lista1_de_numeros.append(numero)

    lista2 = input()
    lista2 = lista2.split()
    lista2_de_numeros = []

    for item in lista2:
        numero = int(item)
        lista2_de_numeros.append(numero)

    intercala_duas_listas(lista1_de_numeros, lista2_de_numeros)

#questão 4
if(var == 's'):
    lista1 = input()
    lista1 = lista1.split()
    lista1_de_numeros = []

    for item in lista1:
        numero = int(item)
        lista1_de_numeros.append(numero)

    lista2 = input()
    lista2 = lista2.split()
    lista2_de_numeros = []

    for item in lista2:
        numero = int(item)
        lista2_de_numeros.append(numero)

    intercala_sem_repeticao(lista1_de_numeros, lista2_de_numeros)

#questão 5 
if(var == 'j'):
    lista1 = input()
    lista1 = lista1.split()
    lista1_de_numeros = []

    for item in lista1:
        numero = int(item)
        lista1_de_numeros.append(numero)

    lista2 = input()
    lista2 = lista2.split()
    lista2_de_numeros = []

    for item in lista2:
        numero = int(item)
        lista2_de_numeros.append(numero)
    
    lista3 = input()
    lista3 = lista3.split()
    lista3_de_numeros = []

    for item in lista3:
        numero = int(item)
        lista3_de_numeros.append(numero)

    intercalar_tres_listas(lista1_de_numeros, lista2_de_numeros, lista3_de_numeros)

#questão 6
if(var == 'f'):
    lista = input()
    lista = lista.split()
    lista_de_numeros = []

    for item in lista:
        numero = int(item)
        lista_de_numeros.append(numero)

    ordena_por_frequencia_de_ocorrencia(lista_de_numeros)

#questão 7
if(var == 'm'):
    lista1 = input()
    lista1 = lista1.split()
    lista1_de_numeros = []

    for item in lista1:
        numero = int(item)
        lista1_de_numeros.append(numero)

    lista2 = input()
    lista2 = lista2.split()
    lista2_de_numeros = []

    for item in lista2:
        numero = int(item)
        lista2_de_numeros.append(numero)

    pares_antes_de_impares_ordena_dentro_da_categoria_e_intercala(lista1_de_numeros, lista2_de_numeros)



