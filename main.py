import os
import os.path
import pprint

listaarch = []
listasize = []
listadir = []

def analizar(path):
        lista = os.listdir(path)
        for elemento in lista:
            elemento_path = f'{path}/{elemento}'

            if os.path.isfile(elemento_path):
                size = round(os.path.getsize(elemento_path) / 1024)
                listaarch.append("nombre: " + str(elemento))
                listasize.append("tamaño: " + str(size) + " kb")

            elif os.path.isdir(elemento_path):
                analizar(elemento_path)
                listadir.append(elemento)


        diccio = dict(zip(listaarch, listasize))
        pprint.pprint("archivos: \n" + str(diccio))
        pprint.pprint("carpetas: \n"+ str(listadir))


analizar("C:/Users/Jinbo Jonez")
