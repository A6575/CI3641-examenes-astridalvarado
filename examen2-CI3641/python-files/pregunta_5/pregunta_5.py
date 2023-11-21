import manejador_datos as mdata
from itertools import takewhile, dropwhile

def main():
    # se le muestra al usuario las opciones disponibles
    print(""" OPERACIONES DISPONIBLES:
        -- ATOMICO <nombre> <representacion> <alineacion>: Define un nuevo tipo atómico de nombre <nombre>, cuya representación 
                                                           ocupa <representacion> bytes y debe estar alineado a <alineacion> bytes.

        -- STRUCT <nombre> [<tipo>]: Define un nuevo registro de nombre <nombre>. La definición de los campos del
                                     registro viene dada por la lista en [<tipo>]

        -- UNION <nombre> [<tipo>]: Define un nuevo registro variante de nombre <nombre>. La definición de los campos
                                    del registro variante viene dada por la lista en [<tipo>].

        -- DESCRIBIR <nombre>: Debe dar la información correspondiente al tipo con nombre <nombre>.

        -- SALIR : salir del simulador 
        """)
    
    manejador_global = mdata.ManejadorDatos()
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
        
        # Si la operacion ingresada es ATOMICO
        if "ATOMICO" in command and len(datatype_as_list) == 3:
            # se realiza un casteo de los datos para poder verificar que:
            error_detection = list(map ( (lambda x: int(x) if x.isdigit() else int(float(x)) if len(x) > 1 and x[0] == "-" else x ) , datatype_as_list ))
            
            # el nombre sea de tipo string
            if type(error_detection[0]) is not str:
                print("\nERROR: nombre ingresado invalido.\n")
                continue
            
            # los valores ingresados sea una lista de enteros
            if any([x for x in error_detection[1:] if type(x) is not int]):
                print("\nERROR: la representacion y la alineacion deben ser del tipo entero.\n")
                continue
            
            # los valores ingresados no sea negativos
            if any([x for x in error_detection[1:] if x < 0]):
                print("\nERROR: la representacion y la alineacion deben ser enteros no negativos.\n")
                continue

            manejador_global.atomico(datatype_as_list)

            # si al momento de intentar agregar un tipo atomico se encuentra un error, se reporta al usuario
            if manejador_global.error_atomico != "":
                print("\n"+manejador_global.error_atomico+"\n")
                continue

            print(f"\nSe ha agregado el tipo de datos {datatype_as_list[0]}, ocupando {datatype_as_list[1]} bytes y alineado a {datatype_as_list[2]} bytes\n")
        
        # si la operacion ingresada es STRUCT
        elif "STRUCT" in command and len(datatype_as_list) > 1:
            manejador_global.struct(datatype_as_list)

            # si al momento de intentar agregar un tipo struct se encuentra un error, se reporta al usuario
            if len(manejador_global.error_struct) == 1:
                print("\n"+manejador_global.error_struct[0]+"\n")
                continue
            
            # si al momento de intentar agregar un tipo struct se encuentra mas de un error, se reporta al usuario
            if len(manejador_global.error_struct) > 1:
                print()
                print("\n".join(manejador_global.error_struct))
                print()
                continue
            
            print(f"\nSe ha agregado el tipo de datos {datatype_as_list[0]} con campos de tipo: "+", ".join(datatype_as_list[1:])+"\n")
        
        # si la operacion ingresada es UNION
        elif "UNION" in command and len(datatype_as_list) > 1:
            manejador_global.union(datatype_as_list)

            # si al momento de intentar agregar un tipo union se encuentra un error, se reporta al usuario
            if len(manejador_global.error_union) == 1:
                print("\n"+manejador_global.error_union[0]+"\n")
                continue
            
            # si al momento de intentar agregar un tipo union se encuentra mas de un error, se reporta al usuario
            if len(manejador_global.error_union) > 1:
                print()
                print("\n".join(manejador_global.error_union))
                print()
                continue
            
            print(f"\nSe ha agregado el tipo de datos {datatype_as_list[0]} con campos de tipo: "+", ".join(datatype_as_list[1:])+"\n")

        # si la operacion ingresada en DESCRIBIR
        elif "DESCRIBIR" in command and len(datatype_as_list) == 1:
            
            manejador_global.describir(datatype_as_list[0])

            # si al momento de describir un tipo de datos se encuentra un error, se reporta al usuario.
            if manejador_global.error_descripcion != "":
                print("\n"+manejador_global.error_descripcion+"\n")
                continue
            
            print(f"\n-------------------- DESCRICION DEL DATO {datatype_as_list[0].upper()} --------------------" )
            print(f"""* EMPAQUETADO:
            >> TAMAÑO TOTAL: {manejador_global.descripcion_dato[0][0]}
            >> ALINEACIÓN TOTAL: {manejador_global.descripcion_dato[0][1]}
            >> DESPERDICIO DE MEMORIA: {manejador_global.descripcion_dato[0][2]}

* NO EMPAQUETADO:
            >> TAMAÑO TOTAL: {manejador_global.descripcion_dato[1][0]}
            >> ALINEACIÓN TOTAL: {manejador_global.descripcion_dato[1][1]}
            >> DESPERDICIO DE MEMORIA: {manejador_global.descripcion_dato[1][2]}

* REORDENADO:
            >> TAMAÑO TOTAL: {manejador_global.descripcion_dato[2][0]}
            >> ALINEACIÓN TOTAL: {manejador_global.descripcion_dato[2][1]}
            >> DESPERDICIO DE MEMORIA: {manejador_global.descripcion_dato[2][2]}
            """)
        else:
            print("\nERROR: Operacion invalida.\n")

    
if __name__ == "__main__":
    main()