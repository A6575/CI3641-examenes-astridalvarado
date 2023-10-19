# IMPORTACION DE FUNCIONES Y VARIABLES GLOBALES 
from diagramaT import *

# funcion principal del programa
def main():
    # se le muestra al usuario las opciones disponibles
    print(""" OPERACIONES DISPONIBLES:
        -- DEFINIR <tipo> [<argumentos>]: definición de clase <tipo> con <argumentos>. Los tipos y argumentos son:
            + PROGRAMA <nombre> <lenguaje> : programa identificado por <nombre> escrito en <lenguaje>
            + INTERPRETE <lenguaje_base> <lenguaje> : intérprete para <lenguaje> escrito en <lenguaje_base>
            + TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino> : traductor desde <lenguaje_origen> hacia <lenguaje_destino>,
                                                                               escrito en <lenguaje_base>
        -- EJECUTABLE <nombre>  : consulta de la posibilidad de ejecutar el programa de nombre <nombre>
        -- SALIR : salir del simulador """)
    
    # Variable para guardar el ultimo lenguaje obtenido
    last_inserted_language = ""
    while True:
        # se obtiene del usuario la operacion a realizar y se almaneca en una lista
        operation = input("Ingrese la operacion a ejecutar: ")
        operation_splited = operation.split(" ")
        
        # terminacion del programa
        if operation_splited[0] == "SALIR":
            print(">> Fin del programa")
            break
        
        if operation_splited[0] == "DEFINIR":
            # si se desea definir un programa, se invoca la funcion correspondiente
            if operation_splited[1] == "PROGRAMA" and len(operation_splited) == 4:
                last_inserted_language = operation_splited[3]
                add_program(operation_splited[2], operation_splited[3])
            
            # si se desea definir un interprete, se invoca la funcion correspondiente
            elif operation_splited[1] == "INTERPRETE" and len(operation_splited) == 4:
                add_inter(operation_splited[2], operation_splited[3])
            
            # si se desea definir un traductor, se invoca la funcion correspondiente
            elif operation_splited[1] == "TRADUCTOR" and len(operation_splited) == 5:
                add_trac(operation_splited[2], operation_splited[3], operation_splited[4])
            
            else:
                print("ERROR: tipo de definicion invalido.")
        
        # si se desea saber si un programa es ejecutable, se invoca la funcion correspondiente
        elif operation_splited[0] == "EJECUTABLE" and len(operation_splited) == 2:
            print(can_execute(operation_splited[1], last_inserted_language))
            
        else:
            print("ERROR: Operacion invalida.")

if __name__ == "__main__":
    main()