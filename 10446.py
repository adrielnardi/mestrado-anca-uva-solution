import fileinput


def trib(n,back):
    if n <=1:
        return 1
    if x[n][back] != 0:
        return x[n][back]

    x[n][back] = 1
    for i in range(back):
        x[n][back] = x[n][back] + trib(n-i,back)
    return x[n][back]


def main():
    caso = 1
    for t in fileinput.input():
        if t == "\n":
            break
        n, back = t.replace("\n", "").split("")
        if n > 60:
            break
        n = int(n)
        back = int(back)
        print(f"Case {caso}: {trib(n,back)}")
        caso = caso+1



if __name__ == "__main__":
    while True:
        try:
            #carrega a matriz com valor 0 em cada i,j da matriz
            x = [[0 for y in range(61)] for x in range(61)]
            #entra no programa principal
            main()
        except EOFError:
            break
        finally:
            exit(0)
