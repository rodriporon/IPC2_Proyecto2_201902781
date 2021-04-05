class Nodo(object):
    def __init__(self, dato, fila, columna):
        self.fila = fila
        self.columna = columna
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.abajo = None
        self.arriba = None

class Header(object):
    def __init__(self, number):
        self.number = number
        self.siguiente = None
        self.anterior = None
        self.valor = None

class HeaderList(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0

    def insertar(self, nuevo):
        if self.inicio == None:
            self.inicio = nuevo
        else:            
            
            if int(nuevo.number) < int(self.inicio.number):
                nuevo.siguiente = self.inicio
                self.inicio.anterior = nuevo
                self.inicio = nuevo
            else:
                temporal = self.inicio
                while temporal.siguiente != None:
                    if int(nuevo.number) < int(temporal.siguiente.number):
                        temporal.siguiente.anterior = nuevo
                        nuevo.anterior = temporal
                        break
                    temporal = temporal.siguiente
                
                if temporal.siguiente == None:
                    temporal.siguiente = nuevo
                    nuevo.anterior = temporal
                
    def retornarEn(self, number):
        temporal = self.inicio        
        while temporal != None:
            if temporal.number == number:
                return temporal
            temporal = temporal.siguiente
        return None
    

class Matriz(object):
    
    def __init__(self, nombre, filas, columnas):
        
        self.encabezadoFilas = HeaderList()
        self.encabezadoColumnas = HeaderList()
        self.siguiente = None
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas


    def insertar(self, dato, fila, columna):
        nuevo = Nodo(dato,fila,columna)
        encabezadoFila = self.encabezadoFilas.retornarEn(fila)
        if encabezadoFila == None:
            encabezadoFila = Header(fila)
            encabezadoFila.valor = nuevo
            self.encabezadoFilas.insertar(encabezadoFila)            
        else: 
            if int(nuevo.columna) < int(encabezadoFila.valor.columna):
                nuevo.derecha = encabezadoFila.valor
                encabezadoFila.valor.izquierda = nuevo
                encabezadoFila.valor = nuevo
            else:
                temporal = encabezadoFila.valor
                while temporal.derecha !=None:
                    if int(nuevo.columna) < int(temporal.derecha.columna):
                        nuevo.derecha = temporal.derecha
                        temporal.derecha.izquierda = nuevo
                        nuevo.izquierda = temporal
                        temporal.derecha = nuevo
                        break
                    temporal = temporal.derecha
                
                if temporal.derecha == None: 
                    temporal.derecha = nuevo
                    nuevo.izquierda = temporal
        encabezadoColumna = self.encabezadoColumnas.retornarEn(columna)
        if encabezadoColumna == None:
            encabezadoColumna = Header(columna)
            self.encabezadoColumnas.insertar(encabezadoColumna)
            encabezadoColumna.valor = nuevo
        else: 
            if int(nuevo.fila) < int(encabezadoColumna.valor.fila):
                nuevo.abajo = encabezadoColumna.valor
                encabezadoColumna.valor.arriba = nuevo
                encabezadoColumna.valor = nuevo
            else:
                temporal = encabezadoColumna.valor
                while temporal.abajo != None:
                    if int(nuevo.fila) < int(temporal.abajo.fila):
                        nuevo.abajo = temporal.abajo
                        temporal.abajo.arriba = nuevo
                        nuevo.arriba = temporal
                        temporal.abajo = nuevo
                        break
                    temporal = temporal.abajo
                if temporal.abajo == None: 
                    temporal.abajo = nuevo
                    nuevo.arriba = temporal

    def get(self, fila, columna):
        encabezadoFila = self.encabezadoFilas.inicio
        while(encabezadoFila != None):
            temporal = encabezadoFila.valor
            while temporal != None:
                if temporal.fila == fila and temporal.columna == columna:
                    return temporal
                temporal = temporal.derecha
            encabezadoFila = encabezadoFila.siguiente

