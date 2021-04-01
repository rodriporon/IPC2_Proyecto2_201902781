
class Nodo(object):
    def __init__(self,fila,columna,datos):
        self.datos = datos
        self.fila = fila
        self.columna= columna
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None
    
class nodoEncabezado(object):
    def __init__(self,id):
        self.id = id
        self.siguiente = None
        self.anterior  = None
        self.accesoNodo = None

class listaEncabezado(object):
    def __init__(self):
        self.primero  = None
        self.count = 0 

    def setEncabezado(self,nuevo):
        if self.primero == None:
            self.primero = nuevo
        elif nuevo.id < self.primero.id:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente != None:
                if nuevo.id < tmp.siguiente.id:
                    nuevo.siguiente = tmp.siguiente
                    tmp.siguiente.anterior = nuevo
                    tmp.anterior= tmp
                    tmp.siguiente = nuevo #NO SE SI SEA NECESARIO RE DIRECCIONAR :()
                    break
                tmp = tmp.siguiente

            if tmp.siguiente == None:
                tmp.siguiente = nuevo
                nuevo.anterior = tmp
    
    #Encontrar Encabezados
    def getEncabezado(self,id):
        tmp = self.primero
        while tmp != None:
            if tmp.id == id:
                return tmp
            tmp = tmp.siguiente
        return None

class matriz:
    def __init__(self,name,filas,columnas):
        self.name = name
        self.filas = filas
        self.columnas = columnas
        self.eFila = listaEncabezado()
        self.eColumna = listaEncabezado()
        self.siguiente = None


    def insertar(self,fila,columna,dato):
        nuevo = Nodo(fila,columna,dato)
        #insercion de encabezado por fila 
        eFila = self.eFila.getEncabezado(fila)
        if eFila == None:
            eFila = nodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFila.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                tmp = eFila.accesoNodo
                while tmp.derecha != None:
                    if nuevo.columna < tmp.derecha.columna:
                        nuevo.derecha = tmp.derecha
                        tmp.derecha.izquierda = nuevo
                        nuevo.izquierda = tmp
                        tmp.derecha = nuevo
                        break
                    tmp = tmp.derecha
                
                if tmp.derecha == None:
                    tmp.derecha = nuevo
                    nuevo.izquierda = tmp
        #Insercion encabezado por columna
        eColumna = self.eColumna.getEncabezado(columna)
        if eColumna ==None:                             #no existe  el encabezado solicitado
            eColumna = nodoEncabezado(columna)          #Crea el nuevo encabezado
            eColumna.accesoNodo = nuevo
            self.eColumna.setEncabezado(eColumna)
        else:                                           #ya existe el encabezado solicitado
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo       #se inserta al inicio de esa lista
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo          #se inserta en medio de la lista
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo        #Se inserta al final de la lista. 
                    nuevo.arriba = actual

    #Recorrido por filas
    def recorrerFilas(self):
        eFila = self.eFila.primero
        print('Recorrido por filas')
        while eFila != None:
            print("\n Fila "+ str(eFila.id))
            actual = eFila.accesoNodo
            while actual != None:
                print( str(actual.datos)+"  " + str(actual.fila)+ ", " + + str(actual.columna))
                actual = actual.derecha
            eFila = eFila.siguiente
        print("-----------------------------------")


    #Retornar nodo por coordenada
    def retornarNodoEn(self,fila,columna):
        eFila = self.eFila.inicio
        while(eFila != None):
            tmp = eFila.accesoNodo
            while tmp != None:
                if tmp.fila==fila and tmp.columna == columna :
                    return tmp
                tmp = tmp.derecha
            eFila = eFila.siguiente


    #Recorrido por colulmnas 
    def recorrerColumnas (self):
        eColumna = self.eColumna.primero
        print("\n  Recorrido por columnas ")
        while eColumna != None:
            tmp = eColumna.accesoNodo
            while tmp != None:
                print(tmp.datos)
                if eColumna.siguiente != None or tmp.abajo != None:
                    print('->')
                tmp = tmp.derecha
            eColumna = eColumna.siguiente
        print("-------------------------------------------")


    def BrecorrerFilas(self):
        eFila = self.eFila.primero
        print("\n ************* Recorrido por filas: ******************")
        while eFila != None:
            actual = eFila.accesoNodo
            print("\n Fila "+ str(actual.fila))
            print("columna        valor")
            while actual != None:
                print(str(actual.columna)+ "         " + str(actual.datos))
                actual = actual.derecha
            eFila = eFila.siguiente
        print("-----------------------------------")


    def BuscaValor(self,x,y):
        tmp = self.inicio

        while tmp is not None:
            if tmp.x == str(x):
                if tmp.y == str(y):
                    return tmp.dato
                else:
                    tmp.siguiente
                tmp=tmp.siguiente
            else:
                tmp = tmp.siguiente

n = matriz('matriz1', 1, 2)

n.insertar(0, 1, 5)
n.insertar(1, 1, 'moy')
n.insertar(1, 2, 'maus')
n.insertar(0, 2, 8)
n.insertar(1, 0, 15)
n.insertar(0, 0, "maria")

n.retornarNodoEn(0,1)
#n.recorrerColumnas()