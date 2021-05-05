#!/usr/bin/env python3
# -- coding: utf-8 --

# 10908 – Largest Square
T, M,N,Q,r,c = 0,0,0,0,0,0
linha, grid, lista, centro = [], [], [],[]


def lendoinput(T):
        for i in range(int(T)):
            linha = input().split(" ")
            M = int(linha[0])
            N = int(linha[1])
            Q = int(linha[2])
            linha.clear()
            print(f'{M} {N} {Q}')
            lista = []

            for i in range(M):
                linha = input().strip()
                lista.append(linha)

            grid = list(map(list, lista))

            for j in range(Q):
                verifica = False
                aux = input().split()
                r = int(aux[0])
                c = int(aux[1])
                largura = 0
                centro = grid[r][c]
                while True:
                    largura += 1
                    indicer = r - largura
                    indicec = c - largura
                    if indicer < 0 or indicec < 0 or r + largura >= M or c + largura >= N:
                        print(largura * 2 - 1)
                        break
                    qtd = 2 * largura + 1
                    for i in range(qtd):
                        for j in range(qtd):
                            if grid[indicer + i][indicec + j] != centro:
                                verifica = True
                    if verifica:
                        print(largura * 2 - 1)
                        break

if __name__ == "__main__":
    while True:
        try:
            T = input()
            lendoinput(T)
        except EOFError:
            exit(3)
        exit(0)





