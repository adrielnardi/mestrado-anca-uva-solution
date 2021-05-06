dicionario = []
senha = []


def gera_regra(regra, i):
	if i == len(regra):
		print(''.join(senha))
		return
	if regra[i] == "0":
		for digito in range(10):
			senha.append(str(digito))
			gera_regra(regra, i + 1)
			senha.pop()
	elif regra[i] == "#":
		for palavra in dicionario:
			senha.append(palavra)
			gera_regra(regra, i + 1)
			senha.pop()


def teste_caso(n):
	global dicionario
	dicionario = []
	for k in range(n):
		palavra = input().strip()
		aux = True
		for i in palavra:
			if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' and (0 < len(palavra) < 256):
				aux = True
			else:
				aux = False
				break
		if aux == True:
			dicionario.append(palavra)
	m = int(input())
	if m < 1000:
		regra = []
		print("--")
		for l in range(m):
			regra = input().strip()

			count = 0
			for r in regra:
				if r == '0':
					count = count + 1

			if 1 <= count <= 7 and len(regra) < 256:
				gera_regra(regra, 0)


if __name__ == "__main__":
	while True:
		try:
			n = int(input())
		except EOFError:
			break
		if 0 < n <= 100:
			teste_caso(n)