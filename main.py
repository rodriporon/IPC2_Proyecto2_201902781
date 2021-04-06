from os import terminal_size
from tkinter import * 
from tkinter import ttk
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from nodo import Nodo
from lista import Lista 
from MatrizOrtogonal import Matriz
from ListaSimple import listaSimple
from NodoLista import nodoLista
from datetime import date
from datetime import datetime
import webbrowser
import os

now = datetime.now()

global nombre_matrices, imagen_matrices, lista_matrices, imagen_mostrar
imagen_mostrar = ''

datos_reporte_cargarmatriz1 = listaSimple()
lista_matrices = Lista()

ventana = Tk()
ventana.title('Ventana Principal')
ventana.state('zoomed')
#ventana.resizable(False, False)

def cargarArchivo():
    global nombre_matrices, imagen_mostrar
    root = Tk()
    root.withdraw()
    root.update()
    root.attributes("-topmost", True)
    pathString = askopenfilename(filetypes=[("Text files","*.xml")])
    #Leída del archivo
    archivo = minidom.parse(pathString)
    cont = archivo.getElementsByTagName('matriz')
    contador = 0
    for matriz in cont:
        nombre = matriz.getElementsByTagName('nombre')[0]
        filas = matriz.getElementsByTagName('filas')[0]
        columnas = matriz.getElementsByTagName('columnas')[0]
        imagen = matriz.getElementsByTagName('imagen')[0]
 
        Lista_Mat = Matriz(nombre.firstChild.data,filas.firstChild.data,columnas.firstChild.data)

        fila = 0
        columna = 0

        for i in imagen.firstChild.data:
            if i == '-':
                imagen_mostrar += ' '
                columna += 1 
            elif i == '*':
                imagen_mostrar += '*'
                columna +=1
                Lista_Mat.insertar(i, fila, columna)
            elif i == '\n':
                imagen_mostrar += '\n'
                columna = 0
                fila += 1
        lista_matrices.insertar(Lista_Mat)
    

    combo['values'] = lista_matrices.Get_Names()


#Realizando operaciones de una sola imagen
def rotacionHorizontal(matriz):

    for i in range(int(get_x(matriz))):
        for j in range(int(get_y(matriz))):
            nodo = Entry(panelResultado, width=3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz.get(get_x(matriz)-i, j+1):
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                nodo.insert(0,'*')
                
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Rotación Horizontal- Matriz: {matriz.nombre}'))
def rotacionVertical(matriz):

    for i in range(int(get_x(matriz))):
        for j in range(int(get_y(matriz))):
            nodo = Entry(panelResultado, width=3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz.get(i+1, get_y(matriz)-j):
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                nodo.insert(0,'*')
                
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Rotación Vertical- Matriz: {matriz.nombre}'))
def traspuesta(matriz):

    for i in range(int(get_x(matriz))):
        for j in range(int(get_y(matriz))):
            nodo = Entry(panelResultado, width=3)
            nodo.grid(padx = 2, pady = 2, row = j, column = i, columnspan = 1)
            if matriz.get(i+1, j+1):
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                nodo.insert(0,'*')    
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Traspuesta- Matriz: {matriz.nombre}')) 

def nuevaVentanaLimpiarArea(matriz):
    ventanaLimpiar = Toplevel(ventana)
    ventanaLimpiar.title('Limpiar área')
    ventanaLimpiar.geometry('350x300')
    Label(ventanaLimpiar, text='Limpiar desde:', font=('Agency FB', 14)).place(x=20, y=30)
    Label(ventanaLimpiar, text='hasta:', font=('Agency FB', 14)).place(x=20, y=90)
    Label(ventanaLimpiar, text='fila', font=('Agency FB', 12)).place(x=160, y=0)
    Label(ventanaLimpiar, text='columna', font=('Agency FB', 12)).place(x=230, y=0)

    desde_fila = Entry(ventanaLimpiar, width=4)
    desde_fila.place(x=160, y=40)

    desde_columna = Entry(ventanaLimpiar, width=4)
    desde_columna.place(x=230, y=40)

    hasta_fila = Entry(ventanaLimpiar, width=4)
    hasta_fila.place(x=160, y=100)
    
    hasta_columna = Entry(ventanaLimpiar, width=4)
    hasta_columna.place(x=230, y=100)


    bot_limpiar_area = Button(ventanaLimpiar, text='Limpiar área', command=lambda:limpiarArea(int(desde_fila.get()), int(desde_columna.get()), int(hasta_fila.get()), int(hasta_columna.get()), combo.get()))
    bot_limpiar_area.place(x=260, y=260)

    

def limpiarArea(desde_fila, desde_columna, hasta_fila, hasta_columna, nombre_matriz):
    for i in range(lista_matrices.cant):
        if nombre_matriz == lista_matrices.get(i+1).nombre:
            matriz_operar = lista_matrices.get(i+1)
    pos_x = get_x(matriz_operar)
    pos_y = get_y(matriz_operar)
    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            nodo = Entry(panelResultado, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_operar.get(i+1, j+1):
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                
def nuevaVentanaLineaHorizontal():
    
    ventanaLineaHorizontal = Toplevel(ventana)
    ventanaLineaHorizontal.title('Linea horizontal')
    ventanaLineaHorizontal.geometry('350x300')
    Label(ventanaLineaHorizontal, text='Agregar linea en:', font=('Agency FB', 14)).place(x=20, y=30)
    Label(ventanaLineaHorizontal, text='No. elementos:', font=('Agency FB', 14)).place(x=20, y=90)
    Label(ventanaLineaHorizontal, text='fila', font=('Agency FB', 12)).place(x=160, y=0)
    Label(ventanaLineaHorizontal, text='columna', font=('Agency FB', 12)).place(x=230, y=0)

    fila = Entry(ventanaLineaHorizontal, width=4)
    fila.place(x=160, y=40)

    columna = Entry(ventanaLineaHorizontal, width=4)
    columna.place(x=230, y=40)

    cantidad_elementos = Entry(ventanaLineaHorizontal, width=4)
    cantidad_elementos.place(x=160, y=100)

    bot_limpiar_area = Button(ventanaLineaHorizontal, text='Agregar Línea', command=lambda:lineaHorizontal(int(fila.get()), int(columna.get()), int(cantidad_elementos.get()), combo.get()))
    bot_limpiar_area.place(x=260, y=260)

def nuevaVentanaVertical():
    
    ventanaLineaVertical = Toplevel(ventana)
    ventanaLineaVertical.title('Linea Vertical')
    ventanaLineaVertical.geometry('350x300')
    Label(ventanaLineaVertical, text='Agregar linea en:', font=('Agency FB', 14)).place(x=20, y=30)
    Label(ventanaLineaVertical, text='No. elementos:', font=('Agency FB', 14)).place(x=20, y=90)
    Label(ventanaLineaVertical, text='fila', font=('Agency FB', 12)).place(x=160, y=0)
    Label(ventanaLineaVertical, text='columna', font=('Agency FB', 12)).place(x=230, y=0)

    fila = Entry(ventanaLineaVertical, width=4)
    fila.place(x=160, y=40)

    columna = Entry(ventanaLineaVertical, width=4)
    columna.place(x=230, y=40)

    cantidad_elementos = Entry(ventanaLineaVertical, width=4)
    cantidad_elementos.place(x=160, y=100)

    bot_limpiar_area = Button(ventanaLineaVertical, text='Agregar Línea', command=lambda:lineaVertical(int(fila.get()), int(columna.get()), int(cantidad_elementos.get()), combo.get()))
    bot_limpiar_area.place(x=260, y=260)   

def nuevaVentanaRectangulo():

    nuevaVentanaRectangulo = Toplevel(ventana)
    nuevaVentanaRectangulo.title('Rectángulo')
    nuevaVentanaRectangulo.geometry('400x300')
    Label(nuevaVentanaRectangulo, text='Dibujar en:', font=('Agency FB', 14)).place(x=20, y=30)
    Label(nuevaVentanaRectangulo, text='anchoxlargo:', font=('Agency FB', 14)).place(x=20, y=90)
    Label(nuevaVentanaRectangulo, text='fila', font=('Agency FB', 12)).place(x=160, y=0)
    Label(nuevaVentanaRectangulo, text='columna', font=('Agency FB', 12)).place(x=230, y=0)

    fila = Entry(nuevaVentanaRectangulo, width=4)
    fila.place(x=160, y=40)

    columna = Entry(nuevaVentanaRectangulo, width=4)
    columna.place(x=230, y=40)

    ancho = Entry(nuevaVentanaRectangulo, width=4)
    ancho.place(x=160, y=100)
    
    largo = Entry(nuevaVentanaRectangulo, width=4)
    largo.place(x=230, y=100)


    bot_limpiar_area = Button(nuevaVentanaRectangulo, text='Agregar Rectángulo', command=lambda:dibujarRectangulo(int(fila.get()), int(columna.get()), int(ancho.get()), int(largo.get()), combo.get()))
    bot_limpiar_area.place(x=260, y=260)

def nuevaVentanaTriangulo():
    ventanaTriangulo = Toplevel(ventana)
    ventanaTriangulo.title('Linea Vertical')
    ventanaTriangulo.geometry('400x300')
    Label(ventanaTriangulo, text='Dibujar en', font=('Agency FB', 14)).place(x=20, y=30)
    Label(ventanaTriangulo, text='Dimensión:', font=('Agency FB', 14)).place(x=20, y=90)
    Label(ventanaTriangulo, text='fila', font=('Agency FB', 12)).place(x=160, y=0)
    Label(ventanaTriangulo, text='columna', font=('Agency FB', 12)).place(x=230, y=0)

    fila = Entry(ventanaTriangulo, width=4)
    fila.place(x=160, y=40)

    columna = Entry(ventanaTriangulo, width=4)
    columna.place(x=230, y=40)

    dimension = Entry(ventanaTriangulo, width=4)
    dimension.place(x=160, y=100)

    bot_limpiar_area = Button(ventanaTriangulo, text='Dibujar Triángulo', command=lambda:dibujarTriangulo(int(fila.get()), int(columna.get()), int(dimension.get()), combo.get()))
    bot_limpiar_area.place(x=260, y=260) 

def dibujarTriangulo(fila, columna, dimension, nombre_matriz):
    for i in range(lista_matrices.cant):
        if nombre_matriz == lista_matrices.get(i+1).nombre:
            matriz_operar = lista_matrices.get(i+1)
    aux_fila = fila
    aux_columna = columna
    pos_x = get_x(matriz_operar)
    pos_y = get_y(matriz_operar)
    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            nodo = Entry(panelResultado, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_operar.get(i+1, j+1):
                aux = 1
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                if(i == (fila+dimension-2)) and (j >= (columna-1) and j <= (columna+dimension-2)):
                    nodo.configure({'background': "#6ec6ff"})
                if(i >= (fila-1) and i <= (fila+dimension-2)) and (j == (columna-1)):
                    nodo.configure({'background': "#6ec6ff"})
                if(i >= (fila-1) and i <= (fila+dimension-2)) and (aux_fila == i) and (aux_columna == j) and (j > (columna-1) and j < (columna+dimension-2)):
                    nodo.configure({'background': "#6ec6ff"})
                    aux_columna += 1
                    aux_fila += 1
            if(i == (fila+dimension-2)) and (j >= (columna-1) and j <= (columna+dimension-2)):
                if not matriz_operar.get(i+1, j+1) and nodo.get() != '*':
                    nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'black')
                nodo.configure({'background': "#6ec6ff"})
            if(i >= (fila-1) and i <= (fila+dimension-2)) and (j == (columna-1)):
                if not matriz_operar.get(i+1, j+1) and nodo.get() != '*':
                    nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'black')
                nodo.configure({'background': "#6ec6ff"})
            if(i >= (fila-1) and i <= (fila+dimension-2)) and (aux_fila == i) and (aux_columna == j) and (j > (columna-1) and j < (columna+dimension-2)):
                if not matriz_operar.get(i+1, j+1) and nodo.get() != '*':
                    nodo.insert(0,'*')
                    paso = True
                nodo.config(justify = 'center', fg = 'black')
                nodo.configure({'background': "#6ec6ff"})
                aux_columna += 1
                aux_fila += 1
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Dibujar Triángulo- Matriz: {nombre_matriz}'))

def dibujarRectangulo(fila, columna, ancho, largo, nombre_matriz):
    paso = False
    for i in range(lista_matrices.cant):
        if nombre_matriz == lista_matrices.get(i+1).nombre:
            matriz_operar = lista_matrices.get(i+1)
    pos_x = get_x(matriz_operar)
    pos_y = get_y(matriz_operar)
    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            nodo = Entry(panelResultado, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_operar.get(i+1, j+1):
                aux = 1
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                if (i == (fila-1)) and (j >= (columna-1)) and (j <= (columna+ancho-2)):
                    nodo.configure({'background': "#6ec6ff"})
                if (i == (fila+largo-2)) and (j >= (columna-1)) and (j <= (columna+ancho-2)):
                    nodo.configure({'background': "#6ec6ff"})
                if (i >= (fila-1)) and (i <= (fila+largo-2)) and (j == (columna+ancho-2)):
                    nodo.configure({'background': "#6ec6ff"})
                if (i >= (fila-1)) and (i <= (fila+largo-2)) and (j == (columna+ancho-2)):
                    nodo.configure({'background': "#6ec6ff"})
            if (i == (fila-1)) and (j >= (columna-1)) and (j <= (columna+ancho-2)): #Horizontal
                if not matriz_operar.get(i+1, j+1) and nodo.get() != '*':
                    nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'black')
                nodo.configure({'background': "#6ec6ff"})
            if (i == (fila+largo-2)) and (j >= (columna-1)) and (j <= (columna+ancho-2)):
                if not matriz_operar.get(i+1, j+1) and nodo.get() != '*':
                    nodo.insert(0,'*')
                    paso = True
                nodo.config(justify = 'center', fg = 'black')
                nodo.configure({'background': "#6ec6ff"})
            if (i >= (fila-1)) and (i <= (fila+largo-2)) and (j == (columna-1)): #Vertical
                if not matriz_operar.get(i+1, j+1) and nodo.get() != '*':
                    nodo.insert(0,'*')
                    paso = True
                nodo.config(justify = 'center', fg = 'black')
                nodo.configure({'background': "#6ec6ff"})
            if (i >= (fila-1)) and (i <= (fila+largo-2)) and (j == (columna+ancho-2)):
                if not matriz_operar.get(i+1, j+1) and nodo.get() != '*':
                    nodo.insert(0,'*')
                    paso = True
                nodo.config(justify = 'center', fg = 'black')
                nodo.configure({'background': "#6ec6ff"})
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Dibujar Rectángulo- Matriz: {nombre_matriz}'))

def lineaHorizontal(fila, columna, cantidad_elementos, nombre_matriz):
    for i in range(lista_matrices.cant):
        if nombre_matriz == lista_matrices.get(i+1).nombre:
            matriz_operar = lista_matrices.get(i+1)
    
    pos_x = get_x(matriz_operar)
    pos_y = get_y(matriz_operar)

    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            nodo = Entry(panelResultado, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_operar.get(i+1, j+1):
                aux = 1
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                if (i >= (fila-1) and (i <= fila-1)) and (j >= (columna-1) and (j <= columna+cantidad_elementos-2)):
                    if aux == 1:
                        pass
                    else:
                        nodo.insert(0, '*')
                    nodo.configure({'background': "#6ec6ff"})
                    nodo.config(justify = 'center', fg = 'black')
            if (i >= (fila-1) and (i <= fila-1)) and (j >= (columna-1) and (j <= columna+cantidad_elementos-2)):
                if not matriz_operar.get(i+1, j+1):
                    nodo.insert(0,'*')
                nodo.configure({'background': "#6ec6ff"})
                nodo.config(justify = 'center', fg = 'black')
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Linea Horizontal - Matriz: {nombre_matriz}'))
def lineaVertical(fila, columna, cantidad_elementos, nombre_matriz):
    for i in range(lista_matrices.cant):
        if nombre_matriz == lista_matrices.get(i+1).nombre:
            matriz_operar = lista_matrices.get(i+1)
    
    pos_x = get_x(matriz_operar)
    pos_y = get_y(matriz_operar)

    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            nodo = Entry(panelResultado, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_operar.get(i+1, j+1):
                aux = 1
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')
                if (i >= (fila-1) and (i <= fila+cantidad_elementos-2)) and (j >= (columna-1) and (j <= columna-1)):
                    if aux == 1:
                        pass
                    else:
                        nodo.insert(0, '*')
                    nodo.configure({'background': "#6ec6ff"})
                    nodo.config(justify = 'center', fg = 'black')
            if (i >= (fila-1) and (i <= fila+cantidad_elementos-2)) and (j >= (columna-1) and (j <= columna-1)):
                if not matriz_operar.get(i+1, j+1):
                    nodo.insert(0,'*')
                nodo.configure({'background': "#6ec6ff"})
                nodo.config(justify = 'center', fg = 'black')
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Linea Vertical - Matriz: {nombre_matriz}'))

def crearPanel():

    panelOriginal = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
    panelOriginal.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')
    panelResultado = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")  
    panelResultado.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nsew')

def clean():
    for child in panelOriginal.winfo_children():
        child.destroy()

    for child in panelResultado.winfo_children():
        child.destroy()

log_nombre_matrices = listaSimple()

def operacionesMatriz(nombre_matriz, opcion):
    imagen = ''
    #print(nombre_matriz)
    for i in range(lista_matrices.cant):
    	if nombre_matriz == lista_matrices.get(i+1).nombre:
    		matriz_operar = lista_matrices.get(i+1)
    if opcion == 0:
        imagenOriginal(matriz_operar)
        
    elif opcion == 1:
        rotacionHorizontal(matriz_operar)
    elif opcion == 2:
        rotacionVertical(matriz_operar)
    elif opcion == 3:
        traspuesta(matriz_operar)
    elif opcion == 4:
        nuevaVentanaLimpiarArea(matriz_operar)
    elif opcion == 4.1:
        limpiarArea(matriz_operar)
    elif opcion == 5:
        nuevaVentanaLineaHorizontal()
    elif opcion == 6:
        nuevaVentanaVertical()
    elif opcion == 7:
        nuevaVentanaRectangulo()
    elif opcion == 8:
        nuevaVentanaTriangulo()
    elif opcion == 9:
        clean()

def operacionesMatriz2():
    ventana_2 = Toplevel(ventana)
    ventana_2.title('Operaciones 2 imagenes')
    ventana_2.state('zoomed')


    frame_combo = Frame(ventana_2, bd=5, relief='raised', bg="#757de8")
    frame_combo.pack()

    matrices = Frame(ventana_2, bd=5, relief='raised',bg="#757de8")
    matrices.pack()
    
    titulo_combo = Label(frame_combo, text='Seleccione las matrices')
    titulo_combo.grid(row=0, column=0, padx=10, pady=5)

    combo_1 = ttk.Combobox(frame_combo, state='readonly')
    combo_1.grid(row=0, column=1, padx=10, pady=5)

    combo_2 = ttk.Combobox(frame_combo, state='readonly')
    combo_2.grid(row=0, column=2, padx=10, pady=5)

    combo_1['values'] = lista_matrices.Get_Names()
    combo_2['values'] = lista_matrices.Get_Names()

    bot_cargar_matrices = Button(frame_combo, text='Cargar matrices', command=lambda:operacionesMatrices(combo_1.get(), combo_2.get(), 0))
    bot_cargar_matrices.grid(row=0, column=3, padx=10, pady=5)

def nuevaVentanaResultMatrices(matriz_1, matriz_2, matriz_mayor_dim, opcion):
    ventana_resultado_matrices = Toplevel(ventana)
    ventana_resultado_matrices.title('Resultado Operaciones 2 Imagenes')
    #ventana_resultado_matrices.state('zoomed')

    matrices = Frame(ventana_resultado_matrices, bd=5, relief='raised',bg="#757de8")
    matrices.pack()

    la_titulo_1 = Label(matrices, text='Imagen Resultante')
    la_titulo_1.grid(row=0, column=0, padx=5, pady=5)

    panel_matrizResultante = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
    panel_matrizResultante.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')

    pos_x = get_x(matriz_mayor_dim)
    pos_y = get_y(matriz_mayor_dim)
    pos_x1 = get_x(matriz_1)
    pos_y1 = get_y(matriz_1)
    pos_x2 = get_x(matriz_2)
    pos_y2 = get_y(matriz_2)

    if opcion == 1:
        for i in range(int(pos_x)): 
            for j in range(int(pos_y)):
                nodo = Entry(panel_matrizResultante, width = 3)
                nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
                if matriz_1.get(i+1, j+1) or matriz_2.get(i+1, j+1):
                    nodo.insert(0,'*')
                    nodo.config(justify = 'center', fg = 'white', bg='#757de8')
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Unión A,B - Matriz 1: {matriz_1.nombre} | Matriz 2: {matriz_2.nombre}'))
    if opcion == 2:
        for i in range(int(pos_x)): 
            for j in range(int(pos_y)):
                nodo = Entry(panel_matrizResultante, width = 3)
                nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
                if matriz_1.get(i+1, j+1) and matriz_2.get(i+1, j+1):
                    nodo.insert(0,'*')
                    nodo.config(justify = 'center', fg = 'white', bg='#757de8')
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Intersección - Matriz 1: {matriz_1.nombre} | Matriz 2: {matriz_2.nombre}'))
    if opcion == 3:
        for i in range(int(pos_x)): 
            for j in range(int(pos_y)):
                nodo = Entry(panel_matrizResultante, width = 3)
                nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
                if matriz_1.get(i+1, j+1) and not matriz_2.get(i+1, j+1):
                    nodo.insert(0,'*')
                    nodo.config(justify = 'center', fg = 'white', bg='#757de8')
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Diferencia A,B - Matriz 1: {matriz_1.nombre} | Matriz 2: {matriz_2.nombre}'))
    if opcion == 4:
        for i in range(int(pos_x)): 
            for j in range(int(pos_y)):
                nodo = Entry(panel_matrizResultante, width = 3)
                nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
                if (matriz_1.get(i+1, j+1) and not matriz_2.get(i+1, j+1)) or (not matriz_1.get(i+1, j+1) and matriz_2.get(i+1, j+1)):
                    nodo.insert(0,'*')
                    nodo.config(justify = 'center', fg = 'white', bg='#757de8')
    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Diferencia Simétrica - Matriz 1: {matriz_1.nombre} | Matriz 2: {matriz_2.nombre}'))
def nuevaVentanaDosMatrices(matriz_1, matriz_2):
    ventana_dos_matrices = Toplevel(ventana)
    ventana_dos_matrices.title('Operaciones 2 imagenes')
    ventana_dos_matrices.state('zoomed')

    menubar = Menu(ventana_dos_matrices)
    ventana_dos_matrices.config(menu=menubar)

    operaciones = Menu(menubar, tearoff=0)
    operaciones.add_command(label='Unión A,B',command=lambda:nuevaVentanaResultMatrices(matriz_1, matriz_2, matriz_mayor_dim, 1))
    operaciones.add_command(label='Intersección A,B',command=lambda:nuevaVentanaResultMatrices(matriz_1, matriz_2, matriz_mayor_dim, 2))
    operaciones.add_command(label='Diferencia A,B',command=lambda:nuevaVentanaResultMatrices(matriz_1, matriz_2, matriz_mayor_dim, 3))
    operaciones.add_command(label='Diferencia Simétrica A,B',command=lambda:nuevaVentanaResultMatrices(matriz_1, matriz_2, matriz_mayor_dim, 4)) 

    menubar.add_cascade(label='Operaciones', menu=operaciones)

    matrices = Frame(ventana_dos_matrices, bd=5, relief='raised',bg="#757de8")
    matrices.pack()

    la_titulo_1 = Label(matrices, text='Imagen Matriz 1')
    la_titulo_2 = Label(matrices, text='Imagen Matriz 2')

    la_titulo_1.grid(row=0, column=0, padx=5, pady=5)
    la_titulo_2.grid(row=0, column=1, padx=5, pady=5)

    panel_matriz1 = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
    panel_matriz1.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')
    panel_matriz2 = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")  
    panel_matriz2.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nsew')

    pos_x1 = get_x(matriz_1)
    pos_y1 = get_y(matriz_1)

    pos_x2 = get_x(matriz_2)
    pos_y2 = get_y(matriz_2)

    dim_matriz1 = pos_x1+pos_y1
    dim_matriz2 = pos_x2+pos_y2

    if dim_matriz1 < dim_matriz2:
        matriz_mayor_dim = matriz_2
    elif dim_matriz1 > dim_matriz2:
        matriz_mayor_dim = matriz_1
    else:
        matriz_mayor_dim = matriz_1

    for i in range(int(pos_x1)): 
        for j in range(int(pos_y1)):
            nodo = Entry(panel_matriz1, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_1.get(i+1, j+1):
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')

    for i in range(int(pos_x2)): 
        for j in range(int(pos_y2)):
            nodo = Entry(panel_matriz2, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_2.get(i+1, j+1):
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')

def operacionesMatrices(matriz_1, matriz_2, opcion):
    for i in range(lista_matrices.cant):
        if matriz_1 == lista_matrices.get(i+1).nombre:
    	    matriz1_operar = lista_matrices.get(i+1)
        if matriz_2 == lista_matrices.get(i+1).nombre:
    	    matriz2_operar = lista_matrices.get(i+1)
    if opcion == 0:
        nuevaVentanaDosMatrices(matriz1_operar, matriz2_operar)
        datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - Matriz 1: {matriz_1} - Espacios llenos : {get_llenos(matriz1_operar)} - Espacios vacíos: {get_vacios(matriz1_operar)} | - Matriz 2: {matriz_2} - Espacios llenos : {get_llenos(matriz2_operar)} - Espacios vacíos: {get_vacios(matriz2_operar)}'))

def get_x(matriz):
	return int(matriz.filas)

def get_y(matriz):
	return int(matriz.columnas)

def get_llenos(matriz):
    pos_x = get_x(matriz)
    pos_y = get_y(matriz)
    lleno = 0
    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            if matriz.get(i+1, j+1):
                lleno += 1
    return lleno   

def get_vacios(matriz):
    pos_x = get_x(matriz)
    pos_y = get_y(matriz)
    vacio = 0
    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            if not matriz.get(i+1, j+1):
                vacio += 1
    return vacio


def imagenOriginal(matriz):
    pos_x = get_x(matriz)
    pos_y = get_y(matriz)

    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            nodo = Entry(panelOriginal, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz.get(i+1, j+1):
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')

    datos_reporte_cargarmatriz1.agregar(nodoLista(f'{datetime.now()} - {matriz.nombre} - Espacios llenos: {get_llenos(matriz)} - Espacios vacíos: {get_vacios(matriz)}'))

def imagenesOriginales(matriz_1, matriz_2):
    pos_x1 = get_x(matriz_1)
    pos_y1 = get_y(matriz_1)

    pos_x2 = get_x(matriz_2)
    pos_y2 = get_y(matriz_2)



    for i in range(int(pos_x1)): 
        for j in range(int(pos_y1)):
            nodo = Entry(panel_matriz1, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_1.get(i+1, j+1):
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')

    for i in range(int(pos_x2)): 
        for j in range(int(pos_y2)):
            nodo = Entry(panel_matriz2, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz_2.get(i+1, j+1):
                nodo.insert(0,'*')
                nodo.config(justify = 'center', fg = 'white', bg='#757de8')

def crearReporte():

    f = open('Reporte.html', 'w', encoding='utf-8')
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="es">\n')
    f.write('<head>\n')
    f.write('<meta charset="utf-8">\n')
    f.write('<title>Reporte</title>\n')
    f.write('<meta name="theme-color" content="#3c790a">\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<div class="container">\n')
    f.write('<article>\n')
    for i in range(datos_reporte_cargarmatriz1.length()):
        f.write(f'<h4><center>{datos_reporte_cargarmatriz1[i]}</h4></center>\n')
    f.write('</article>\n')
    f.write('</div>\n')
    f.write('</body>\n')
    f.write('</html>>\n')
    f.close()
    webbrowser.open_new_tab('Reporte.html')

def datosEstudiante():
    f = open('DatosEstudiante.html', 'w', encoding='utf-8')
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="es">\n')
    f.write('<head>\n')
    f.write('<meta charset="utf-8">\n')
    f.write('<title>Datos del estudiante</title>\n')
    f.write('<meta name="theme-color" content="#3c790a">\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<div class="container">\n')
    f.write('<article>\n')
    f.write('<h4><center>Nombre: Rodrigo Antonio Porón De León</h4></center>\n')
    f.write('<h4><center>Carné: 201902781</h4></center>\n')
    f.write('<h4><center>Curso: Introducción a la programación y computación 2</h4></center>\n')
    f.write('</article>\n')
    f.write('</div>\n')
    f.write('</body>\n')
    f.write('</html>>\n')
    f.close()
    webbrowser.open_new_tab('DatosEstudiante.html')

def abrirDocumentacion():
    ruta = "Ensayo-Proyecto-2.pdf"
    os.popen(ruta)

#Creando el menú superior
menubar = Menu(ventana)
ventana.config(menu=menubar)

cargararchivo = Menu(menubar, tearoff=0)
cargararchivo.add_command(label='Cargar archivo', command=cargarArchivo)

operaciones = Menu(menubar, tearoff=0)
operaciones.add_command(label='Rotación Horizontal',command=lambda:operacionesMatriz(combo.get(),1))
operaciones.add_command(label='Rotación Vertical',command=lambda:operacionesMatriz(combo.get(),2))
operaciones.add_command(label='Traspuesta de una imagen',command=lambda:operacionesMatriz(combo.get(),3))
operaciones.add_command(label='Limpiar zona',command=lambda:operacionesMatriz(combo.get(),4))
operaciones.add_command(label='Agregar línea horizontal',command=lambda:operacionesMatriz(combo.get(),5))
operaciones.add_command(label='Agregar línea vertical',command=lambda:operacionesMatriz(combo.get(),6))
operaciones.add_command(label='Agregar rectángulo',command=lambda:operacionesMatriz(combo.get(),7))
operaciones.add_command(label='Agregar triángulo rectángulo',command=lambda:operacionesMatriz(combo.get(),8))
operaciones.add_command(label='Limpiar',command=lambda:operacionesMatriz(combo.get(),9))

operaciones_2 = Menu(menubar, tearoff=0)
operaciones_2.add_command(label='Operaciones con 2 imagenes',command=operacionesMatriz2)

reportes = Menu(menubar, tearoff=0)
reportes.add_command(label='Crear Reporte', command=crearReporte)

ayuda = Menu(menubar, tearoff=0)
ayuda.add_command(label='Datos del estudiante', command=datosEstudiante)
ayuda.add_command(label='Ver documentación', command=abrirDocumentacion)

menubar.add_cascade(label='Cargar Archivo', menu=cargararchivo)
menubar.add_cascade(label='Operaciones 1 imagen', menu=operaciones)
menubar.add_cascade(label='Operaciones 2 imagenes', menu=operaciones_2)
menubar.add_cascade(label='Reportes', menu=reportes)
menubar.add_cascade(label='Ayuda', menu=ayuda)


#creando los frames
frame_combo = Frame(ventana, bd=5, relief='raised', bg="#757de8")
frame_combo.pack()

matrices = Frame(ventana, bd=5, relief='raised',bg="#757de8")
matrices.pack()

#Creando combobox
titulo_combo = Label(frame_combo, text='Seleccione la matriz')
titulo_combo.grid(row=0, column=0, padx=10, pady=5)
combo = ttk.Combobox(frame_combo, state='readonly')
combo.grid(row=0, column=1, padx=10, pady=5)
bot_cargar_matriz = Button(frame_combo, text='Cargar Matriz', command=lambda:operacionesMatriz(combo.get(),0))
bot_cargar_matriz.grid(row=0, column=2, padx=10, pady=5)

#Creando labels
la_titulo_1 = Label(matrices, text='Imagen Matriz Original')
la_titulo_2 = Label(matrices, text='Imagen Matriz Resultado')

#Creando Panels
panelOriginal = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
panelOriginal.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')
panelResultado = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")  
panelResultado.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nsew')
panel_limpiarArea = Frame(ventana)

panel_matriz1 = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
panel_matriz2 = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
#Insertando botones
""" bot_cargar_archivo.grid(row=0, column=0, padx=50, pady=5)
bot_operaciones.grid(row=0, column=1, padx=50, pady=5)
bot_reportes.grid(row=0, column=2, padx=50, pady=5)
bot_ayuda.grid(row=0, column=3, padx=50, pady=5)
 """

#Insertando labels
la_titulo_1.grid(row=0, column=0, padx=5, pady=5)
la_titulo_2.grid(row=0, column=1, padx=5, pady=5)


ventana.mainloop()
#Rama features