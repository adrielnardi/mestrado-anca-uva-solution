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



if __name__ == "__main__":
    while True:
        try:
            #carrega a matriz com valor 0 em cada i,j da matriz
            x = [[0 for y in range(61)] for x in range(61)]
            #entra no programa principal
            caso = 1
            print(f"Case {caso}: {trib(3, 3)}")
            caso = caso + 1
            print(f"Case {caso}: {trib(4, 4)}")
            caso = caso + 1
            print(f"Case {caso}: {trib(5, 5)}")
            caso = caso + 1
            print(f"Case {caso}: {trib(6, 6)}")
            caso = caso + 1
            print(f"Case {caso}: {trib(7, 7)}")
            caso = caso + 1
            print(f"Case {caso}: {trib(8, 8)}")
            caso = caso + 1
            print(f"Case {caso}: {trib(9, 9)}")
            caso = caso + 1
            print(f"Case {caso}: {trib(61, 61)}")
            caso = caso + 1


        except EOFError:
            break
        finally:
            exit(0)
