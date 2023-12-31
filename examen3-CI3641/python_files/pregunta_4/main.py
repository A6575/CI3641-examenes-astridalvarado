import vtable as vt
from itertools import takewhile, dropwhile

def main():
    # se le muestra al usuario las opciones disponibles
    print(""" OPERACIONES DISPONIBLES:
        -- CLASS <tipo> [<nombre>]: Define un nuevo tipo que poseerá métodos con nombres establecidos en la lista proporcionada.
                                    El <tipo> puede ser:
                                • Un nombre, que establece un tipo que no hereda de ningún otro.
                                • Una expresión de la forma <nombre> : <super>, que establece el nombre del tipo y el 
                                                                       hecho de que este tipo hereda del tipo con nombre <super>.

        -- DESCRIBIR <nombre>: muestra la tabla de métodos virtuales para el tipo con el nombre propuesto.

        -- SALIR : salir del simulador 
        """)
    
    manejador_global = vt.ManejadorVtable()
    while True:
        # se obtiene del usuario la operacion a realizar
        operation = input("Ingrese la operacion a ejecutar: ")
        command = "".join(list(takewhile((lambda x: x != " "), operation)))
        datatype = "".join(list(dropwhile((lambda x: x != " "), operation))[1:])
        datatype_as_list = datatype.split(" ")
        
        # terminacion del programa
        if command == "SALIR":
            print("\n>> Fin del programa\n")
            break
        
         # Si la operacion ingresada es CLASS
        if "CLASS" in command:
            # si existe : en la lista de datos, se considera que el tipo tiene una superclase
            if ":" in datatype_as_list:
                # se separan los datos en 3 partes: nombre, superclase y atributos
                subclase = datatype_as_list[0]
                superclase = datatype_as_list[2]
                atributos = datatype_as_list[3:]
                # se definen las clases
                manejador_global.definir_clase(subclase, atributos, superclase)
                
                # si existe algun error, se reporta el mismo
                if manejador_global.error_clase != "" or manejador_global.error_superclase != "" or manejador_global.error_atributos != "":
                    print("\n".join([manejador_global.error_clase, manejador_global.error_superclase, manejador_global.error_atributos]))
                else:
                    print(f"Se ha definido una nueva subclase {subclase} de {superclase} con atributos: "+", ".join(atributos))
            else:
                # si no existe : en la lista de datos, se considera que el tipo no tiene una superclase
                # se separan los datos en 2 partes: nombre y atributos
                clase = datatype_as_list[0]
                atributos = datatype_as_list[1:]
                # se definen las clases
                manejador_global.definir_clase(clase, atributos)
                
                 # si existe algun error, se reporta el mismo
                if manejador_global.error_clase != "" or manejador_global.error_superclase != "" or manejador_global.error_atributos != "":
                    print("\n".join([manejador_global.error_clase, manejador_global.error_superclase, manejador_global.error_atributos]))
                else:            
                    print(f"Se ha definido una nueva clase {clase} con atributos: "+", ".join(atributos))
    
        # si la operacion ingresada en DESCRIBIR
        elif "DESCRIBIR" in command and len(datatype_as_list) == 1:
            # se obtiene la descripcion de la clase
            metodos_clase = manejador_global.describir_clase(datatype_as_list[0])
            
            # si se encuentra que no existe la clase a describir, se reporta error
            if manejador_global.error_clase != "":
                print(manejador_global.error_clase)
            else:
                print(f"---- TABLA DE METODOS VIRTUALES DE {datatype_as_list[0]} ----")
                for metodos, clases in metodos_clase:
                    for met in metodos:
                        print(f"\t\t{met} -> {clases} :: {met}")
        else:
            print("\nERROR: Operacion invalida.\n")

if __name__ == "__main__":
    main()