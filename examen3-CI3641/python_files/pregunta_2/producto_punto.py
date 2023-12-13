import threading
from queue import Queue

def producto_punto(v1, v2):
    """
    Calcula el producto punto entre dos vectores
    usando threads concurrentes
    """

    # se valida que los vectores tengan la misma longitud
    try:
        n = len(v1)
        m = len(v2)
    
        if n != m:
            raise ValueError("Los vectores deben tener la misma longitud")
        
    except ValueError as ve:
        print(ve)
        return

    resultado = 0
    
    def producto_punto(start, end, q):
        """
        Función que realiza el producto_punto para un rango dado
        """
        suma_parcial = 0
        for i in range(start, end):
            suma_parcial += v1[i] * v2[i]
        q.put(suma_parcial)
    
    parte = n // 4 # Dividir el proceso en 4 partes para poder crear los hilos de forma concurrente
    
    # lista para almacenar los hilos creados
    threads = []
    # cola para la comunicacion entre hilos
    q = Queue()
    for i in range(4):
        # se calcula el rango para cada parte
        start = i * parte
        end = (i+1) * parte if i < 3 else n
        # se crea los hilos para cada parte
        thread = threading.Thread(target=producto_punto, args=(start, end, q))
        # se almacenan los hilos en la lista
        threads.append(thread)
        # y se inician cada uno de ellos
        thread.start()
    
    # luego, para cada hilo
    for thread in threads:
        # se espera a que termine su ejecucion
        thread.join()
        # se obtiene el resultado del hilo
        resultado += q.get()
    
    # finalmente, se retorna el resultado
    return resultado


if __name__ == "__main__":
    # Ejemplo    
    v1 = [1,2,3,5,3] 
    v2 = [0,2,1,3,9]
    
    print("Vector v1:", v1)
    print("Vector v2:", v2)
    print("El resultado es:",producto_punto(v1, v2))