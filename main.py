from tkinter import *
from tkinter.filedialog import askopenfilename

ventana = Tk()
ventana.title('Ventana Principal')
ventana.geometry('800x700')
#ventana.resizable(False, False)

def cargarArchivo():
    root = Tk()
    root.withdraw()
    root.update()
    root.attributes("-topmost", True)
    pathString = askopenfilename(filetypes=[("Text files","*.lfp")])
    la_imagen_ori = Label(matrices, text=pathString)
    la_imagen_res = Label(matrices, text=pathString)
    la_imagen_ori.grid(row=1, column=0, padx=10, pady=5)
    la_imagen_res.grid(row=1, column=1, padx=10, pady=5)
    

#creando los frames
menu = Frame(ventana, bd=5, relief='raised', bg="#757de8")
menu.pack()

matrices = Frame(ventana, bd=5, relief='raised',bg="#757de8")
matrices.pack()

#Creando botones
bot_cargar_archivo = Button(menu, text='Cargar Archivo', command= cargarArchivo)
bot_operaciones = Button(menu, text='Operaciones')
bot_reportes = Button(menu, text='Reportes')
bot_ayuda = Button(menu, text='Ayuda')

#Creando labels
la_titulo_1 = Label(matrices, text='Imagen Matriz Original')
la_titulo_2 = Label(matrices, text='Imagen Matriz Resultado')

#Insertando botones
bot_cargar_archivo.grid(row=0, column=0, padx=50, pady=5)
bot_operaciones.grid(row=0, column=1, padx=50, pady=5)
bot_reportes.grid(row=0, column=2, padx=50, pady=5)
bot_ayuda.grid(row=0, column=3, padx=50, pady=5)

#Insertando labels
la_titulo_1.grid(row=0, column=0, padx=5, pady=5)
la_titulo_2.grid(row=0, column=1, padx=5, pady=5)




ventana.mainloop()
