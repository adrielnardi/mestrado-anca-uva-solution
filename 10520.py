import fileinput

def main():

    for l in fileinput.input():
        if l == "\n":
            break

        linha = l.split()
        n = int(linha[0])
        an1 = int(linha[1])
        for i in range(1,n+1):
            for j in range(1,n+1):
                a[i][j]=-1
        a[n][1]= an1
        print(a)

if __name__ == "__main__":
    while True:
        try:
            #carrega a matriz com valor 0 em cada i,j da matriz
            a = [[0 for y in range(23)] for x in range(23)]
            #entra na função def main()
            main()
        except EOFError:
            break
        finally:
            exit(0)
