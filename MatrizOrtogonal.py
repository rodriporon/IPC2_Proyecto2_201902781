class Header:
    def __init__(self, index, siguiente=None, anterior=None):
        self.index = index
        self.siguiente = siguiente
        self.anterior = anterior
        self.nodoInterno = None

class NodoInterno:
    def __init__(self, valor, derecha=None, izquierda=None, arriba=None, abajo=None):
        self.derecha = derecha
        self.izquierda = izquierda
        self.arriba = arriba
        self.abajo = abajo
        self.valor = valor
        self.x = None
        self.y = None

class ListHeader:
    def __init__(self):
        self.primero = None
            
    def insertHeader(self, index):
        nuevoNodo = Header(index)
        if self.primero == None:
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
        return nuevoNodo

    def buscar(self, index):
        aux = self.primero
        while(aux):
            if(aux.index == index):
                return aux
            aux = aux.siguiente
        return None


class Matriz:
    def __init__(self):
        self.headerX = ListHeader()
        self.headerY = ListHeader()

    def insertar(self, valor, x, y):
        headX = self.headerX.buscar(x)
        headY = self.headerY.buscar(y)
        nuevoElemento = NodoInterno(valor)
        if (headX):
            headX = headX
        else:
            self.headerX.insertHeader(x)
        if (headY):
            headY = headY
        else:
            headY = self.headerY.insertHeader(y)
        nuevoElemento.x = headX
        nuevoElemento.y = headY
        self.insertarHorizontal(headY, nuevoElemento, x)
        self.insertarVertical(headX, nuevoElemento, y)

    def insertarVertical(headX, nuevoElemento, index):
        if(not headX.nodoInterno):
            headX.nodoInterno = nuevoElemento
        else:
            if(index < headX.nodoInterno.y.index):
                nuevoElemento.abajo = headX.nodoInterno
                headX.nodoInterno.arriba = nuevoElemento
                headX.nodoInterno = nuevoElemento
            else:
                aux = headX.nodoInterno
                auxanterior = aux
                while(aux and index > aux.y.index):
                    auxanterior = aux
                    aux = aux.abajo
                if(aux):
                    nuevoElemento.abajo = aux
                    nuevoElemento.arriba = aux.arriba
                    aux.arriba.abajo = nuevoElemento
                    aux.arriba = nuevoElemento
                else:
                    auxanterior.abajo = nuevoElemento
                    nuevoElemento.anterior = auxanterior

    def insertarHorizontal(headY, nuevoElemento, index):
        if(not headY.nodoInterno):
            headY.nodoInterno = nuevoElemento
        else:
            if(index < headY.nodoInterno.x.index):
                nuevoElemento.derecha = headY.nodoInterno
                headY.nodoInterno.izquierda = nuevoElemento
                headY.nodoInterno = nuevoElemento
            else:
                aux = headY.nodoInterno
                auxanterior = aux
                while(aux and index > aux.x.index):
                    auxanterior = aux
                    aux = aux.derecha
                if(aux):
                    print(aux)
                    print(index)
                    nuevoElemento.derecha = aux
                    nuevoElemento.izquierda = aux.izquierda
                    aux.izquierda.derecha = nuevoElemento
                    aux.izquierda = nuevoElemento
                else:
                    auxanterior.derecha = nuevoElemento
                    nuevoElemento.izquierda = auxanterior

    def imprimir(self):
        auxy = self.headerY.primero
        while(auxy):
            auxx = auxy.nodoInterno
            cadena = ''
            while(auxx):
                cadena += f'[{auxx.valor}]'
                auxx += auxx.derecha
            print(str(cadena))
            auxy = auxy.siguiente


matriz = Matriz()
matriz.insertar('a', 1,1)

matriz.imprimir()