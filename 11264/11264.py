

def coin():
    T = int(input())

    if T >= 1 and T <=1000:

        for _ in range(T):
            nmoedas = int(input())
            moedas = list(map(int, input().split()))
            resposta = soma = 0

            if nmoedas < 1000000000:

                for _ in range(nmoedas):
                    for i, moeda in enumerate(moedas[:-1]):
                        #greedy property
                        if soma + moeda < moedas[i + 1]:
                            soma += moeda
                            resposta += 1
                print(resposta+1)


if __name__ == "__main__":
    coin()
