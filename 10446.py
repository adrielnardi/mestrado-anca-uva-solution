import fileinput

for t in fileinput.input():
    if t == "\n":
        break;
    n,back = t.split(" ")
    n = int(n)
    valor = int(back)
    print(n)
    print(back)
