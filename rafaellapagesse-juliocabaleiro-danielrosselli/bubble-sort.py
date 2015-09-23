import matplotlib.pyplot as plt

lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
N = 20
y= lista
x= range(0,N,1)

plt.figure()
plt.title("Estado inicial")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.plot(x, y, "ok")
plt.savefig("bubble-inicio.png")
plt.close()


print ("Lista original:" , lista)
for i in range (0,N-1,1):
    for j in range (i+1,N,1):
        if lista[i]>lista[j]:
	    tmp = lista[i]
	    lista[i] = lista [j]
	    lista[j] = tmp

plt.figure()
plt.title("Estado final")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.plot(x, y, "ok")
plt.savefig("bubble-fim.png")
plt.close()















