# Inicio de la secuencia fibonacci y posicion
fibo=[1,2]
pos=0

# Crear secuencia
while True:
	num=fibo[pos]+fibo[pos+1] 
	if num<4000000:
	   fibo.append(num)
	   pos+=1
	else:
	  break

# Extraer pares y sumarlos
pares=sum([x for x in fibo if x%2==0])
print(f'La suma de todos los pares menores de 4 millones en la secuencia fibonacci es {pares}')
