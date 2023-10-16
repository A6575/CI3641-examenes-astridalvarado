# Importacion de la libreria sys para el manejo de argumentos 
import sys
# Modulo buddy_system con todas las funciones necesarias para el programa
import buddy_system

# Funcion main del programa
def main():
    # En primer lugar, se verifica que se haya pasado la cantidad de bloques a utilizar 
    if len(sys.argv) == 1 :
        print("ERROR: debe indicar la cantidad de bloques a utilizar. Ejemplo:\npy | python | python3 pregunta3.py [cantidad-bloques]")
    elif len(sys.argv) == 2:
        # si se dio la cantidad de argumentos, se verifica que sea no-negativo
        if int(sys.argv[1]) < 0:
            print("ERROR: la cantidad de bloques no puede ser un numero negativo")
        else:
            # Se crea un objeto del tipo Buddy_System pasando como parametro la cantidad total de bloques a usar
            bs = buddy_system.Buddy_System(int(sys.argv[1]))
            # Mensaje informativo con las operaciones disponibles
            print(""" OPERACIONES DISPONIBLES:
        -- RESERVAR <cantidad> <nombre> : reserva de espacio de <cantidad> bloques, asociados al identificador <nombre>
        -- LIBERAR <nombre> : liberación del espacio que contiene el identificador <nombre>
        -- MOSTRAR : mostrar una representación gráfica de listas de bloques libres e información de nombres con su memoria asociada
        -- SALIR : salir del simulador """)
            
            while True:
                # Se le pide al usuario que ingrese una accion a ejecutar y se genera un arreglo con la operacion y sus demas argumentos
                operation = input("Ingrese una operacion: ")
                operation_splited = operation.split(" ")

                # Si el primer elemento del arreglo es SALIR, se termina el programa
                if operation_splited[0] == "SALIR":
                    print(">> Fin del programa")
                    break
                
                # Si el primer elemento del arreglo es MOSTRAR, se muesta al usuario es estado de la simulacion
                if operation_splited[0] == "MOSTRAR":
                    bs.mostrar()
                
                # Si el primer elemento es LIBERAR y este tiene todos los argumentos necesarios para ser ejecutado,
                # se llama al metodo liberar de la clase buddy system
                elif operation_splited[0] == "LIBERAR" and len(operation_splited) == 2:
                    bs.liberar(operation_splited[1])
                
                # Si el primer elemento es RESERVAR y este tiene todos los argumentos necesarios para ser ejecutado,
                # se llama al metodo reservar de la clase buddy system
                elif operation_splited[0] == "RESERVAR" and len(operation_splited) == 3:
                    bs.reservar(operation_splited[1], operation_splited[2])
                else:
                    # Para cualquier otra operacion ingresada, se indica error
                    print("ERROR: operacion invalida\n")
    else:
        print("ERROR: cantidad de argumentos pasados invalida. Solo se debe pasar la cantidad de bloques como argumento. Ejemplo:\npy | python | python3 pregunta3.py [cantidad-bloques]")

if __name__ == "__main__":
    main()