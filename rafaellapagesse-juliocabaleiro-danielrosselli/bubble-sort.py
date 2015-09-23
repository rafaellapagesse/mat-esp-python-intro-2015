import matplotlib.pyplot as plt

lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
N = 20
print ("Lista original:" , lista)
y= lista
x= range(0,N,1)

plt.figure()
plt.title("Estado inicial")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.plot(x, y, "ok")
plt.savefig("fig/bubble-inicio.png")
plt.close()
#esse for define o intervalo de 0 a N-1, andando de 1 em 1.
for i in range (0,N-1,1):
#esse for vê o número seguinte ao i, até N, andando de 1 em 1.
    for j in range (i+1,N,1):
        a = 0 
#esse if define se elas estão ou não em ordem.
        if lista[i]>lista[j]:
            tmp = lista[i]
            lista[i] = lista[j]
            lista[j] = tmp
            plt.figure()
            plt.title("Iteracao {}".format(a+1))
            plt.xlabel("Indice")
            plt.ylabel("Valor")
            plt.plot(x, y, "ok")
            plt.savefig("fig/bubble-troca-{}.png".format(a+1))
            plt.close()
            a = a+1            
#imprime a lista organizada		
print("Lista em ordem crescente:", lista)
#imprimir os cinco maiores valores da lista [Inicial:Final:de qnt em qnt anda] - o inicio é fechado, o fim é intervalo aberto.
print("Cinco maiores valores:", lista[N-1:N-6:-1])
#imprimir os cinco menores valores da lista [Inicial:Final:de qnt em qnt anda]
print("Cinco menores valores:", lista[0:5:1])

plt.figure()
plt.title("Estado final")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.plot(x, y, "ok")
plt.savefig("fig/bubble-fim.png")
plt.close()
















