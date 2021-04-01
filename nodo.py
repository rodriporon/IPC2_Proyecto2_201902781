class Nodo:
    def __init__(self, valor=None, anterior=None, siguiente=None):
        self.valor = valor
        self.anterior = anterior
        self.siguiente = siguiente 

    def __str__(self):
        resultado = str(self.valor)
        return resultado