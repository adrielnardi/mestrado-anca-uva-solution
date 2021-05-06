#!/usr/bin/env python3
# -- coding: utf-8 --
cadeia = ""
proximo = 1
tam_descartada = 0
maximo = 500


def gerarPedaco(indice):
    global cadeia
    global ultimo
    global proximo
    global tam_descartada
    tam_cadeia = len(cadeia)
    aux = ''
    cadeia_aux = ''

    if tam_cadeia > maximo:
        tam_descartada += len(cadeia)
        cadeia = ""

    tam_cadeia_fictica = len(cadeia) + tam_descartada

    for i in range(1, proximo+1):
        aux += str(i)

    proximo += 1
    cadeia_aux += aux
    tam_cadeia_fictica += len(aux)

    while tam_cadeia_fictica < indice:
        aux += str(proximo)
        cadeia_aux += aux
        tam_cadeia_fictica += len(aux)
        proximo += 1

    cadeia += cadeia_aux


def pegarResposta(ind):
    global tam_descartada
    global cadeia
    indice_real = (ind - tam_descartada) - 1

    if indice_real < len(cadeia):
        return cadeia[indice_real]
    else:
        gerarPedaco(ind)
        indice_real = (ind - tam_descartada) - 1
        return cadeia[indice_real]


if __name__ == "__main__":
    lista = []
    while True:
        try:
            T = int(input())
            for i in range(T):
                linha = input()
                if linha != '':
                    linha = int(linha)
                    lista.append(linha)

        except EOFError:
            break
        #resposta = lista[:]
        auxlista = lista[:]
        auxlista.sort()
        for j in auxlista:
            resp = pegarResposta(j)
            x = lista.index(j)
            lista[x] = resp

        for j in lista:
            print(j)

        exit(0)