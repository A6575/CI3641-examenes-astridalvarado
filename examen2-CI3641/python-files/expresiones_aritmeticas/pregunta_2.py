import aritmetica as arit
from itertools import takewhile, dropwhile

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
        
        # Se obtiene el comando ingresado
        command = "".join(list(takewhile((lambda x: not arit.es_Expresion(x)), operation)))

        # Se obtiene la expresion
        expr = arit.Expresion("".join(list(dropwhile((lambda x: not arit.es_Expresion(x)), operation))))

        # Listas para el manejo de posibles errores
        numbers_in_expr = [x for x in expr.expression_as_list if type(x) is int]                                                # Lista de numeros de la expresion
        operations_in_expr = [x for x in expr.expression_as_list if type(x) is not int]                                         # Lista de simboloes en la expresion
        unexpected_chars = [x for x in operations_in_expr if x not in arit.operators]                                           # Lista de caracteres inesperados
        unexpected_operators = [x for x in operations_in_expr if any([y for y in x if len(x) > 1 and y in arit.operators])]     # Lista de operadores inesperados

        # terminacion del programa
        if command == "SALIR":
            print(">> Fin del programa")
            break
        
        if len(unexpected_operators) > 0:
            # Se imprime un mensaje de error si existen operadores unido a un numero
            print("ERROR: caracter(es) inesperado(s) en la expresion ingresada:", ", ".join(unexpected_operators))
            continue

        if len(unexpected_chars) > 0 and "" not in unexpected_chars:
            # Se imprime un mensaje de error si existen caracteres distintos a +, /, - y *
            print("ERROR: caracter(es) inesperado(s) en la expresion ingresada:", ", ".join(unexpected_chars))
            continue

        if any([x for x in numbers_in_expr if x<0]):
            # Se imprime un mensaje de error si se ingresaron numeros negativos
            print("ERROR: no se admiten numeros negativos.")
            continue

        if len(operations_in_expr) + 1 > len(numbers_in_expr):
            # Se imprime un mensaje de error si se hay insuficientes numeros 
            print("ERROR: cantidad insuficiente de numeros en la expresion.")
            continue
        
        if len(operations_in_expr) + 1 < len(numbers_in_expr):
            # Se imprime un mensaje de error si se hay exceso de numeros
            print("ERROR: la expresion dada cuenta con demasiados numeros")
            continue
        
        # Si la operacion ingresada es EVAL
        if "EVAL" in command:
            # si es de tipo PRE y hay expresion ingresada
            if "PRE" in command and expr.expression != "":
                # Se verifica que la primera posicion sea un numero y la ultima posicion sea un operador
                # para lanzar un error
                if expr.expression[0].isdigit() or expr.expression[-1] in arit.operators:
                    print("ERROR: la operacion ingresada no es una expresion prefija")
                    continue
                
                # si se obtiene un caracter vacio en la lista de expresiones, quiere decir que hay espacios demas
                # en la expresion
                if "" in expr.expression_as_list:
                    print("ERROR: existe uno o mas espacios demas en la expresion ingresada.")
                    continue

                expr.eval("PRE")
                print("El resultado es:", expr.stack[0])
            
             # si es de tipo POST y hay expresion ingresada
            elif "POST" in command and expr.expression != "":
                # Se verifica que la primera posicion sea un operador y la ultima posicion sea un numero
                # para lanzar un error
                if expr.expression[0] in arit.operators or expr.expression[-1] not in arit.operators:
                    print("ERROR: la operacion ingresada no es una expresion postfija")
                    continue

                # si se obtiene un caracter vacio en la lista de expresiones, quiere decir que hay espacios demas
                # en la expresion
                if "" in expr.expression_as_list:
                    print("ERROR: existe uno o mas espacios demas en la expresion ingresada.")
                    continue

                expr.eval("POST")
                print("El resultado es:", expr.stack[0])
            
            else:
                print("ERROR: orden de operacion invalido.")
        
        # si la operacion ingresada es MOSTRAR
        elif "MOSTRAR" in command:
            if "PRE" in command and expr != "":
                # Se verifica que la primera posicion sea un numero y la ultima posicion sea un operador
                # para lanzar un error
                if expr.expression[0].isdigit() or expr.expression[-1] in arit.operators:
                    print("ERROR: la operacion ingresada no es una expresion prefija")
                    continue
                
                # si se obtiene un caracter vacio en la lista de expresiones, quiere decir que hay espacios demas
                # en la expresion
                if "" in expr.expression_as_list:
                    print("ERROR: existe uno o mas espacios demas en la expresion ingresada.")
                    continue

                expr.mostrar("PRE")
                print("La expresion ingresada es:", expr.infix_stack[0])
            elif "POST" in command and expr != "":
                # Se verifica que la primera posicion sea un operador y la ultima posicion sea un numero
                # para lanzar un error
                if expr.expression[0] in arit.operators or expr.expression[-1] not in arit.operators:
                    print("ERROR: la operacion ingresada no es una expresion postfija")
                    continue
                
                # si se obtiene un caracter vacio en la lista de expresiones, quiere decir que hay espacios demas
                # en la expresion
                if "" in expr.expression_as_list:
                    print("ERROR: existe uno o mas espacios demas en la expresion ingresada.")
                    continue

                expr.mostrar("POST")
                print("La expresion ingresada es:", expr.infix_stack[0])
            else:
                print("ERROR: orden de operacion invalido.")       
        else:
            print("ERROR: Operacion invalida.")
    
if __name__ == "__main__":
    main()