from NodoLista import nodoLista

class listaSimple(nodoLista):
    def __init__(self):
        super().__init__()
        self.cabeza = nodoLista()
        self.contador = 0
        self.valor = self.__str__()
        self.frecuencia = 1
        self.indice_frecuencia = None
        
    def agregar(self, nuevo_nodo):
        nodo = self.cabeza
        while(nodo.siguiente):
            nodo = nodo.siguiente
        nodo.siguiente = nuevo_nodo
        self.contador += 1
        self.valor = self.__str__()
        
    def get(self, i):
        if (i >= self.contador):
            return None
        nodo = self.cabeza.siguiente
        n = 0
        while(nodo):
            if (n == i):
                return nodo
            nodo = nodo.siguiente
            n += 1

    def __getitem__(self, i):
        return self.get(i)

    def length(self):
        return self.contador

    def primero(self):
        return self.get(0)

    def ultimo(self):
        return self.get(self.length() - 1)

    def __str__(self):
        resultado = "["
        for i in range(self.length()):
            nodo = self.get(i)
            if (i == self.length()-1):
                resultado += '{}'.format(nodo.valor)
                break
            resultado += '{}, '.format(nodo.valor)
        resultado += "]"
        return resultado

