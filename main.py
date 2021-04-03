from os import terminal_size
from tkinter import *
from tkinter import ttk
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from nodo import Nodo
from lista import Lista 
from matrizOrtogonal import Matriz

global nombre_matrices, imagen_matrices, lista_matrices, imagen_mostrar
imagen_mostrar = ''

lista_matrices = Lista()

ventana = Tk()
ventana.title('Ventana Principal')
ventana.geometry('800x700')
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
def Giro_Horizontal(matriz):
    T_X = get_x(matriz)
    T_Y = get_y(matriz)

    print(T_X)
    print(T_Y)
    for i in range(int(T_X)):  #10
        for j in range(int(T_Y)):#10 
            celda = Entry(panelResultado, width=3)
            celda.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz.get(T_X-i, j+1) != None:
                celda.insert(0,'*')
                celda.configure({'background': "#757de8"})
                celda.config(justify = 'center', fg = 'white')

def crearPanel():

    panelOriginal = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
    panelOriginal.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')
    panelResultado = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")  
    panelResultado.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nsew')

def limpiar():
    for child in panelOriginal.winfo_children():
        child.destroy()

    for child in panelResultado.winfo_children():
        child.destroy()

def cargarMatriz2(nombre_matriz,option):
    imagen = ''
    pos = ''
    print(nombre_matriz)
    for i in range(lista_matrices.cant):
    	if nombre_matriz == lista_matrices.Get_Objet(i+1).nombre:
    		pos = lista_matrices.Get_Objet(i+1)
    if option == 0:
        image_Origin(pos)
    elif option == 1:
        Giro_Horizontal(pos)
    elif option == 2:
        limpiar()

def get_x(Bname):
	size_X = int(Bname.filas)
	return size_X 

def get_y(Bname):
	size_Y = int(Bname.columnas)
	return size_Y

def image_Origin(matriz):
    pos_x = get_x(matriz)
    pos_y = get_y(matriz)

    for i in range(int(pos_x)): 
        for j in range(int(pos_y)):
            nodo = Entry(panelOriginal, width = 3)
            nodo.grid(padx = 2, pady = 2, row = i, column = j, columnspan = 1)
            if matriz.get(i+1, j+1) != None:
                nodo.insert(0,'*')
                nodo.configure({'background': "#757de8"})
                nodo.config(justify = 'center', fg = 'white')


#Creando el menú superior
menubar = Menu(ventana)
ventana.config(menu=menubar)

cargararchivo = Menu(menubar, tearoff=0)
cargararchivo.add_command(label='Cargar archivo', command=cargarArchivo)

operaciones = Menu(menubar, tearoff=0)
operaciones.add_command(label='Giro Horizontal',command=lambda:cargarMatriz2(combo.get(),1))
operaciones.add_command(label='Limpiar',command=lambda:cargarMatriz2(combo.get(),2))

reportes = Menu(menubar, tearoff=0)
ayuda = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Cargar Archivo', menu=cargararchivo)
menubar.add_cascade(label='Operaciones', menu=operaciones)
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
bot_cargar_matriz = Button(frame_combo, text='Cargar Matriz', command=lambda:cargarMatriz2(combo.get(),0))
bot_cargar_matriz.grid(row=0, column=2, padx=10, pady=5)

#Creando labels
la_titulo_1 = Label(matrices, text='Imagen Matriz Original')
la_titulo_2 = Label(matrices, text='Imagen Matriz Resultado')

#Creando Panels
panelOriginal = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")
panelOriginal.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'nsew')
panelResultado = Frame(matrices, borderwidth = 2, relief = 'raised', bg="#6ec6ff")  
panelResultado.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'nsew')


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