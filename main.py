from os import terminal_size
from tkinter import *
from tkinter import ttk
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from nodo import Nodo
from lista import Lista
from matriz import Matriz

global nombre_matrices, imagen_matrices, lista_matrices, imagen_mostrar
imagen_mostrar = ''
nombre_matrices = Lista()
imagen_matrices = Lista()
lista_matrices = Lista()

ventana = Tk()
ventana.title('Ventana Principal')
ventana.geometry('800x700')
#ventana.resizable(False, False)

def cargarArchivo():
    global nombre_matrices, imagen_mostrar
    lista_nodos = Lista()
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

        lista_matrices.agregar(Matriz(filas.firstChild.data,columnas.firstChild.data,nombre.firstChild.data))
        lista = Lista()
        for i in imagen.firstChild.data:
            if i == '-':
                imagen_mostrar += ' '
                lista.agregar(Nodo(' '))
            elif i == '*':
                imagen_mostrar += '*'
                lista.agregar(Nodo('*'))
            elif i == '\n':
                imagen_mostrar += '\n'
                lista_matrices[contador].agregar(lista)
                lista = Lista()
        contador += 1


        nombre_matrices.agregar(Nodo(nombre.firstChild.data))
        imagen_matrices.agregar(Nodo(imagen.firstChild.data))
    

    combo['values'] = nombre_matrices.mostrarValores()

def cargarMatriz(nombre_matriz):
    imagen = ''
    for i in range(lista_matrices[0].length()):
        print(lista_matrices[0][i])

    la_imagen_ori.insert(INSERT, imagen)
    la_imagen_res.insert(INSERT, ' ')





#Creando el menú superior
menubar = Menu(ventana)
ventana.config(menu=menubar)

cargararchivo = Menu(menubar, tearoff=0)
cargararchivo.add_command(label='Cargar archivo', command=cargarArchivo)
operaciones = Menu(menubar, tearoff=0)
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
bot_cargar_matriz = Button(frame_combo, text='Cargar Matriz', command=lambda:cargarMatriz(combo.get()))
bot_cargar_matriz.grid(row=0, column=2, padx=10, pady=5)

#Creando labels
la_titulo_1 = Label(matrices, text='Imagen Matriz Original')
la_titulo_2 = Label(matrices, text='Imagen Matriz Resultado')

#Creando Texts
la_imagen_ori = Text(matrices)
la_imagen_ori.grid(row=1, column=0, padx=10, pady=5)
la_imagen_ori.config(width=20, height=20, font=('Consolas', 12))


la_imagen_res = Text(matrices)
la_imagen_res.grid(row=1, column=1, padx=10, pady=5)
la_imagen_res.config(width=20, height=20, font=('Consolas', 12))

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
