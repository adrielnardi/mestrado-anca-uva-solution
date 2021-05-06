lista = []
count = 0


def catcher(lista):
    qtd = len(lista)
    auxlista = [0]*qtd
    auxlista[0] = 1
    for i in range(1,qtd):
        maxinter = 1
        for j in range(i):
            if lista[i] <= lista[j] and auxlista[j] + 1 > maxinter:
                maxinter = auxlista[j] + 1
        auxlista[i] = maxinter
    return max(auxlista)


if __name__ == '__main__':
    lista = []
    count = 0
    while True:
        n = int(input())
        if n == -1:
            count += 1
            print(f'Test #{count}:')
            print(f'  maximum possible interceptions: {catcher(lista)}')
            lista = []
            n1 = int(input())
            if n1 == -1:
                break
            else:
                print("")
                lista.append(n1)
        else:
            lista.append(n)
