#mostra a lista original
print ("lista_original = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]")
#define num de elementos
a = "A lista em ordem crescente:"
N = 20 
#define a lista
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
#esse for ...
for i in range (0,N-1,1):
#esse for ...
	for j in range (i+1,N,1):
#esse if ...
		if lista[i]>lista[j]:
			tmp=lista[i]
			lista[i]=lista [j]
			lista[j]=tmp
#imprime a lista organizada		
print(a, lista)












