from nodo import Nodo
from lista import Lista

class Matriz(Lista):
    #m > filas
    #m > cols
    def __init__(self, m, n, nombre):
        self.m = m
        self.n = n
        self.nombre = nombre
        super().__init__()

    def obtener_elem(self, x, y):
        if((y >= self.m) or (x >= self.n)):
            raise RuntimeError('Límites no definidos en la matriz')
        fila = self.get(y)
        celda = fila.get(x)
        return celda.valor

    def get_name(self, nombre):
        name = self.get(nombre)
        return name

    def get_n(self):
        return self.n

    def get_m(self):
        return self.m

    def __str__(self):
        resultado = "["
        for i in range(self.length()):
            nodo = self.get(i)
            if (i == self.length()-1):
                resultado += '{}'.format(nodo.valor)
                break
            resultado += '{},\n'.format(nodo.valor)
        resultado += "]"
        return resultado