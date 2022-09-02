palindromos = []
for n1 in range(100,1000):
	for n2 in range (100, 1000):
		res = str(n1*n2)
		if res==res[::-1]:
			palindromos.append(int(res))
print(f'El palindromo mas grande tras multiplicar 2 numeros de 3 cifras es {palindromos[-1]}')
