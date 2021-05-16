import fileinput
r = 0

def aij(n, i, j):
    r = a[i][j]
    if r != -1:
        return r
    if i < j:
        k = i
        while k < j:
            r = max(r, aij(n, i, k) + aij(n, k + 1, j))
            k = k + 1
    else:
        r0,r1=0,0
        if i < n:
            k = i + 1
            while k <= n:
                r0 = max(r0, aij(n, k, 1) + aij(n, k, j))
                k = k + 1
        if j > 0:
            k = 1
            while k < j:
                r1 = max(r1, aij(n, i, k) + aij(n, n, k));
                k = k + 1
        r = r0 + r1
    a[i][j] = r
    return a[i][j]



def main():

    for l in fileinput.input():
        if l == "\n":
            break

        linha = l.split()
        n = int(linha[0])

        for i in range(n+1):
            for j in range(n+1):
                a[i][j] = -1

        an1 = int(linha[1])

        a[n][1] = an1
        print(aij(n, 1, n))


if __name__ == "__main__":
    while True:
        try:
            #carrega a matriz com valor 0 em cada i,j da matriz
            a = [[0 for y in range(21)] for x in range(21)]
            #entra na função def main()
            main()

        except EOFError:
            break
        finally:
            exit(0)
