from xml.dom import minidom

archivo = minidom.parse('entrada.xml')
cont = archivo.getElementsByTagName('matriz')

for matriz in cont:
    nombre = matriz.getElementsByTagName('nombre')[0]
    filas = matriz.getElementsByTagName('filas')[0]
    columnas = matriz.getElementsByTagName('columnas')[0]
    imagen = matriz.getElementsByTagName('imagen')[0]
    for i in imagen.firstChild.data:
        print(i)
    print(imagen.firstChild.data)