import fileinput


if __name__ == "__main__":
    while True:
        try:
            for t in fileinput.input():
                if t == "0 0":
                    break
                linha = t.split()
                n = int(linha[0])
                k = int(linha[1])
                print(f"{n} {k}")

        except EOFError:
            break
        finally:
            exit(0)
