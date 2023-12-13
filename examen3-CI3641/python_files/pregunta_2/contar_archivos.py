import threading
import os
from queue import Queue

# Cola global para la comunicacion entre hilos
queue = Queue()

# funcion para contar archivos a traves de una ruta
def contar_archivos_carpetas(path):
    # se inicializa el contador en 1 para que asi un directorio se cuente a si mismo
    total = 1
    
    # Si la ruta no ha sido especificada, se reporta error
    try:
        n = len(path)
    
        if n == 0:
            raise ValueError("Debe proporcionar una ruta para realizar el conteo")
        
    except ValueError as ve:
        print(ve)
        return

    # se itera por los subarboles del directorio raiz
    for dir_raiz, directorios, archivos in os.walk(path):
        # se actualiza el total de carpetas y archivos encontrados en el directorio actual
        total += len(archivos) + len(directorios)
        
        # se itera por los subdirectorios encontrado en el directorio actual
        for d in directorios:
            # y para cada uno de estos se crea un hilo
            t = threading.Thread(target=contar_archivos_carpetas, args=(os.path.join(dir_raiz, d),))
            # inicializacion del hilo
            t.start()
    
    # se almacena en la cola el resultado encontrado
    queue.put(total)

if __name__ == '__main__':
    # variable que contiene la ruta raiz
    path = '../../../examen3-CI3641'
    # se llama a la funcion
    contar_archivos_carpetas(path)
    # se obtiene el total de la cola global. Este sera
    # el ultimo elemento de la cola
    total = queue.queue[-1]
    print(f"Total carpetas y archivos encontrados en {path} es: {total}")

