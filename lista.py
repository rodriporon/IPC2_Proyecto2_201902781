#Clase Funcional
class Lista:
    def __init__(self):
        self.cant = 0
        self.inicio = None       
    
    def insertar(self, nuevo):        
        if self.inicio is None:
            self.inicio = nuevo
            self.inicio.siguiente = self.inicio
            self.cant +=1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.cant +=1
            else:
                temporal = self.inicio            
                while temporal.siguiente != self.inicio:
                    temporal = temporal.siguiente
                temporal.siguiente = nuevo
                nuevo.siguiente = self.inicio
                self.cant +=1
    
    def Get_Objet(self, indice):
        temporal = self.inicio
        contador = 1
        while contador < indice:
            contador+=1
            temporal = temporal.siguiente
        return temporal

    def Get_Names(self):
        tmp = self.inicio
        size = 0
        resultado = ''
        spacio = '\n'
        for i in range(int(self.cant)):
            if tmp.nombre !=None:
                resultado += f'{tmp.nombre}'
            tmp=tmp.siguiente
            resultado += f'{ spacio }'
        return resultado