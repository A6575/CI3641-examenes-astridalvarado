def main():
    # se le muestra al usuario las opciones disponibles
    print(""" OPERACIONES DISPONIBLES:
        -- EVAL <orden> <expr>: evaluación de la expresión en <expr>, que está escrita de acuerdo a <orden>. El orden es:
            + PRE : expresiones escritas en orden pre-fijo.
            + POST : expresiones escritas en orden post-fijo.
        -- MOSTRAR <orden> <expr> : impresión en orden in-fijo de la expresión en <expr>, que está escrita de acuerdo a <orden>
        -- SALIR : salir del simulador """)
    
    while True:
        # se obtiene del usuario la operacion a realizar 
        operation = input("Ingrese la operacion a ejecutar: ")
        command = ""
        # terminacion del programa
        if command == "SALIR":
            print(">> Fin del programa")
            break
        
        # Si la operacion ingresada es EVAL
        if "ATOMICO" in command:
            pass
        # si la operacion ingresada es MOSTRAR
        elif "STRUCT" in command:
            pass
        elif "UNION" in command:
            pass
        elif "DESCRIBIR" in command:
            pass
        else:
            print("ERROR: Operacion invalida.")
    
if __name__ == "__main__":
    main()