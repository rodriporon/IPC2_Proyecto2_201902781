from nodo1 import nodoEncabezado,Nodo
from List_Encab import listaEncabezado

class matriz:
    def __init__(self):
        self.eFila = listaEncabezado()
        self.eColumna = listaEncabezado()

    def insertar(self,fila,columna,valor):
        nuevo = Nodo(fila,columna,valor)
        #insercion de encabezado por fila 
        eFila = self.eFila.getEncabezado(fila)
        if eFila ==None:
            eFila = nodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFila.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual
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

    def recorrerFilas(self):
        eFila = self.eFila.primero
        print("\n ************* Recorrido por filas: ******************")
        while eFila != None:
            actual = eFila.accesoNodo
            print("\n Fila "+ str(actual.fila))
            print("columna        valor")
            while actual != None:
                print(str(actual.columna)+ "         " + str(actual.valor))
                actual = actual.derecha
            eFila = eFila.siguiente
        print("-----------------------------------")
    
    def recorrerColumnas (self):
        eColumna = self.eColumna.primero
        print("\n *************** Recorrido por columnas ************")
        while eColumna != None:
            actual = eColumna.accesoNodo
            print("\n Columna"+ str(actual.columna) )
            print("Fila        Valor")
            while actual != None:
                print(str(actual.fila) + "             " + str(actual.valor))
                actual = actual.abajo
            eColumna = eColumna.siguiente
        print("-------------------------------------------")


        

n = matriz()

n.insertar(0, 1, 5)
n.insertar(1, 1, 'moy')
n.insertar(1, 2, 'maus')
n.insertar(0, 2, 8)
n.insertar(1, 0, 15)
n.insertar(0, 0, "maria")

n.recorrerFilas()
n.recorrerColumnas()               
