
#define a lista
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
#define num de elementos
N = 20 
#mostra a lista original
print ("Lista original:" , lista)
#esse for define o intervalo de 0 a N-1, andando de 1 em 1.
for i in range (0,N-1,1):
#esse for vê o número seguinte ao i, até N, andando de 1 em 1.
	for j in range (i+1,N,1):
#esse if define se elas estão ou não em ordem.
		if lista[i]>lista[j]:
			tmp=lista[i]
			lista[i]=lista [j]
			lista[j]=tmp
#imprime a lista organizada		
print("Lista em ordem crescente:", lista)
#imprimir os cinco maiores valores da lista [Inicial:Final:de qnt em qnt anda] - o inicio é fechado, o fim é intervalo aberto.
print("Cinco maiores valores:", lista[N-1:N-6:-1])
#imprimir os cinco menores valores da lista [Inicial:Final:de qnt em qnt anda]
print("Cinco menores valores:", lista[0:5:1])


















