from itertools import dropwhile

# operadores validos
operators = ["+", "/", "-", "*"]

# funcion para saber si un caracter es un caracter valido para una expresion
def es_Expresion(symbol:str):
    return (symbol in operators or symbol.isdigit())

# funcion para realizar los calculos
def calculator(op:str, n1:int, n2:int):
    match op:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 // n2

# clase Expresion para representar expresiones con operaciones post-fijas y pre-fijas
class Expresion():
    # constructor para las expresiones
    def __init__(self, expr: str) -> None:
        # expresion ingresada
        self.expression = expr
        # stack para la evaluacion de la expresion
        self.stack = []
        # stack para mostrar la expresion de maneja in-fija
        self.infix_stack = []
        # lista con los elementos de la expresion con las conversiones necesarias
        self.expression_as_list = list(map ( (lambda x: int(x) if x.isdigit() else int(float(x)) if len(x) > 1 and x[0] == "-" else x ) , self.expression.split(" ") ))
        # lista con los elementos de la expresion
        self.infix_expression_as_list = self.expression.split(" ")
    
    # funcion de evaluacion
    def eval(self, orden: str):
        # en caso de que sea prefijo
        if orden == "PRE":
            # se itera por la expresion
            for elems in self.expression_as_list:
                # y para cada operador encontrado se agrega a la pila
                if elems in operators:
                    self.stack.append(elems)
                # si es un numero, se inicia la evaluacion
                if type(elems) is int:
                    # se agrega el elemento
                    self.stack.append(elems)
                    # y mientras el stack tenga mas de un elemento y el elemento anterior al actual sea
                    # a su vez un numero
                    while len(self.stack)>1 and type(self.stack[-2]) is int:
                        # se realiza el calculo
                        result = calculator(self.stack[-3], self.stack[-2], self.stack[-1])
                        # se eliminar los ultimos 3 elementos de la pila
                        self.stack = self.stack[:-3]
                        # y se agrega el nuevo resultado
                        self.stack.append(result)
        
        # en caso de que sea post-fijo
        if orden == "POST":
            # se itera por la expresion
            for elems in self.expression_as_list:
                # si el elemento actual es un operador
                if elems in operators:
                    # se agrega a la pila
                    self.stack.append(elems)
                    # y si el stack tiene mas de un elemento y los dos elementos posteriores al operador son numeros
                    if len(self.stack)>1 and type(self.stack[-2]) is int and type(self.stack[-3]) is int:
                        # se realiza el calculo
                        result = calculator(self.stack[-1], self.stack[-3], self.stack[-2])
                        # se eliminan los 3 ultimos numeros de la pia
                        self.stack = self.stack[:-3]
                        # y se agrega el resultado
                        self.stack.append(result)
                
                # si el elemento es un entero, se agrega a la pila
                if type(elems) is int:
                    self.stack.append(elems)
    
    # funcion para mostrar la expresion
    def mostrar(self, orden:str):
        # diccionario con la prioridad de los operadores
        priority = {"+": 1, "-": 1, "*": 2, "/": 2}
        
        # si el orden es prefijo, se obtiene la expresion al reves
        if orden == "PRE":
            self.infix_expression_as_list.reverse()
        
        # se itera por los elementos de la expresion
        for elems in self.infix_expression_as_list:
            # cuando se encuentra un operador
            if elems in operators:
                # se obtienen los dos operandos actuales
                op1 = self.infix_stack[-2]
                op2 = self.infix_stack[-1]
                # se sacan de la pila
                self.infix_stack = self.infix_stack[:-2]
                # variables para saber si los operandos actuales no son numeros
                op1_is_not_number = False
                op2_is_not_number = False

                # si existe algun operador en el operando 1
                if any([x for x in operators if x in op1]):
                    # se indica que no es un numero y se extrae su simbolo
                    op1_is_not_number = True
                    inner_symbol_op1 = list(dropwhile((lambda x: x not in operators), op1))[0]
                
                 # si existe algun operador en el operando 2
                if any([x for x in operators if x in op2]):
                    # se indica que no es un numero y se extrae su simbolo
                    op2_is_not_number = True
                    inner_symbol_op2 = list(dropwhile((lambda x: x not in operators), op2))[0]

                # si el operador 2 no es un numero y la prioridad del simbolo interno es menor al operador actual
                if op2_is_not_number and priority[inner_symbol_op2] < priority[elems]:
                    # se agregan parentesis
                    op2 = f"({op2})"

                # si el operador 1 no es un numero y la prioridad del simbolo interno es menor al operador actual
                if op1_is_not_number and priority[inner_symbol_op1] < priority[elems]:
                    # se agregan parentesis
                    op1 = f"({op1})"

                # Si el orden es prefijo, se agrega a la pila alternando los operandos
                if orden == "PRE":
                    self.infix_stack.append(f"{op2} {elems} {op1}")
                
                # Si el orden es postfijo, se agrega a la pila en el orden correspondiente
                if orden == "POST":
                    self.infix_stack.append(f"{op1} {elems} {op2}")
            else:
                # en otro caso, se agrega a la pila los numeros encontrados
                self.infix_stack.append(elems)