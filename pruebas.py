from lista import Lista
from nodo import Nodo
from matriz import Matriz

lista = Lista()
lista.agregar(Nodo(1))
lista.agregar(Nodo(2))
lista.agregar(Nodo(3))

print(lista)

matriz = Matriz(2, 3, 'matriz1')

matriz.agregar(lista)
matriz.agregar(lista)

for i in range(matriz.get_m()):
    for j in range(matriz.get_n()):
        print(matriz[i][j])