class Header:
    def __init__(self, index, siguiente=None, anterior=None):
        self.index = index
        self.siguiente = siguiente
        self.anterior = anterior
        self.nodoInterno = None

class ListHeader:
    def __init__(self):
        self.primero = None
    def insertHeader(self, index):
        nuevoNodo = Header(index)
        if(not self.primero):
            self.primero = nuevoNodo
        else:
            if(index < self.primero.index):
                self.primero.anterior = nuevoNodo
                nuevoNodo.siguiente = self.primero
                self.primero = nuevoNodo
            else:
                aux = self.primero
                auxanterior = aux
                while(aux and index > aux.index):
                    auxanterior = aux
                    aux = aux.siguiente
                if(aux):
                    nuevoNodo.siguiente = aux
                    nuevoNodo.anterior = aux.anterior
                    aux.anterior.siguiente = nuevoNodo
                    aux.anterior = nuevoNodo
                else:
                    auxanterior.siguiente = nuevoNodo
                    nuevoNodo.anterior = auxanterior

                    