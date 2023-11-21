import math

datatype_atomico = {}
datatype_struct = {}
datatype_union = {}

# funcion para calcular la descripcion del dato en modo empaquetado
def calcular_descripcion_empaquetado(fields, lista_descripcion):
    # si el nombre es de un tipo atomico
    if fields in datatype_atomico.keys():
        # se aumenta el tamaño total
        lista_descripcion[0] += datatype_atomico[fields][0]
        # se aumenta el alineamiento total
        lista_descripcion[1] += 4*math.ceil(datatype_atomico[fields][0]/4)
        # finalmente se retorna la lista
    # si el nombre es de un tipo union
    elif fields in datatype_union.keys():
        # se itera por todos lo elementos que la conforman y se llama recursivamente la funcion
        for elems in datatype_union[fields]:
            lista_descripcion = calcular_descripcion_empaquetado(elems, lista_descripcion)
    else:
        # en otro caso, nos encontramos en un tipo de datos struct
        # se itera por todos lo elementos que la conforman y se llama recursivamente la funcion
        for elems in datatype_struct[fields]:
            lista_descripcion = calcular_descripcion_empaquetado(elems, lista_descripcion)
    
    # finalmente se retorna la lista
    return lista_descripcion
    
def calcular_descripcion_no_empaquetado(fields, lista_descripcion, stack):
    # si el tipo de datos es de tipo atomico
    if fields in datatype_atomico.keys():
        paso = datatype_atomico[fields][1]
        for i in range(len(stack)):
            if stack[math.ceil(paso*i/4)] == 4:
                count = 0
                it = math.ceil(paso*i/4)
                amount = datatype_atomico[fields][0]
                for x in range(math.ceil(paso*i/4)):
                    if count + 4 < amount:
                        stack[it] = 0
                    else:
                        stack[it] = 4 - (amount - count)
                        lista_descripcion[2] += stack[it]
                    it += 1
                    count += 4
                break
        # actualizamos el tamaño utilizado
        lista_descripcion[0] += 4*math.ceil(datatype_atomico[fields][0]/4)
        lista_descripcion[1] += datatype_atomico[fields][1]
    # si el tipo de datos es de tipo union
    elif fields in datatype_union.keys():
        # se itera por todos los elementos que la conforman
        stack_tmp = [4]*200
        for elems in datatype_union[fields]:
            list_tmp, stack_tmp = calcular_descripcion_no_empaquetado(elems, [0,0,0],stack_tmp)
            lista_descripcion[0] += 4*math.ceil(list_tmp[0]/4)
            lista_descripcion[1] += list_tmp[1]
            lista_descripcion[2] += 4*math.ceil(list_tmp[0]/4) - list_tmp[0]
    else:
        stack_tmp = [4]*200
        for elems in datatype_struct[fields]:
            list_tmp, stack_tmp = calcular_descripcion_no_empaquetado(elems, [0,0,0],stack_tmp)
            lista_descripcion[0] += 4*math.ceil(list_tmp[0]/4)
            lista_descripcion[1] += list_tmp[1]
            lista_descripcion[2] += 4*math.ceil(list_tmp[0]/4) - list_tmp[0]
        
    return (lista_descripcion, stack)

def calcular_descripcion_reordenado(fields, lista_descripcion):
        
    return lista_descripcion

# clase para el Manejador de datos
class ManejadorDatos():
    # constructor de la clase
    def __init__(self) -> None:
        self.dict_atomico = {}          # valor para guardar el diccionario con los tipo de datos ATOMICOS
        self.error_atomico = ""         # valor para guardar el error encontrado al guardar un tipo ATOMICO
        self.dict_struct = {}           # valor para guardar el diccionario con los tipo de datos STRUCT
        self.error_struct = []          # valor para guardar los errores encontrados al guardar un tipo STRUCT
        self.dict_union = {}            # valor para guardar el diccionario con los tipo de datos UNION
        self.error_union = []           # valor para guardar los errores encontrados al guardar un tipo UNION
        self.descripcion_dato = []      # valor para guardar la informacion recolectada del dato
        self.error_descripcion = ""     # valor para guardar el error encontrado al momento de describir
    
    # funcion para la actualizacion de los tipos ATOMICOS
    def atomico(self, information):
        self.error_atomico = ""
        # si el nombre a ingresar no se encuentra en ningun diccionario
        if information[0] not in datatype_atomico.keys() and information[0] not in datatype_struct.keys() and information[0] not in datatype_union.keys():
            # se agrega el dato con la representacion y alineacion respectiva
            datatype_atomico[information[0]] = (int(information[1]), int(information[2]))
            # y se actualiza el atributo correspondiente
            self.dict_atomico = datatype_atomico
        else:
            # en caso contrario, se almacena el error correspondiente.
            self.error_atomico = f"{information[0]} ya corresponde a un tipo de datos del programa"

    # funcion para la actualizacion de los tipos STRUCT
    def struct(self, information):
        self.error_struct = []
        error_list = []
        # si el nombre a ingresar no se encuentra en ningun diccionario
        if information[0] not in datatype_struct.keys() and information[0] not in datatype_atomico.keys() and information[0] not in datatype_union.keys():
            # se itera sobre los tipos a agregar
            for types in information[1:]:
                # si un tipo de datos no ha sido definido en algun diccionario, se guarda el error en la lista de errores
                if types not in datatype_atomico.keys() and types not in datatype_union.keys() and types not in datatype_struct.keys():
                    error_list.append(f"ERROR: {types} no ha sido definido como tipo de datos")
            
            # si no se ha encontrado error, se almacena el tipo de datos
            if len(error_list) == 0:
                datatype_struct[information[0]] = information[1:]
                # y se actualiza el atributo correspondiente
                self.dict_struct =  datatype_struct
            else:
                # en caso contrario, se almacena la lista de errores correspondientes
                self.error_struct = error_list
        else:
            # en caso contrario, se almacena la lista con el error correspondiente
            self.error_struct = [f"ERROR: {information[0]} ya fue definido como un tipo de datos"]

    # funcion para la actualizacion de los tipos UNION
    def union(self, information):
        self.error_union = []
        error_list = []
        # si el nombre a ingresar no se encuentra en ningun diccionario
        if information[0] not in datatype_union.keys() and information[0] not in datatype_atomico.keys() and information[0] not in datatype_struct.keys():
            # se itera sobre los tipos a agregar
            for types in information[1:]:
                # si un tipo de datos no ha sido definido en algun diccionario, se guarda el error en la lista de errores
                if types not in datatype_atomico.keys() and types not in datatype_struct.keys() and types not in datatype_union.keys():
                    error_list.append(f"ERROR: {types} no ha sido definido como tipo de datos")
            
            # si no se ha encontrado error, se almacena el tipo de datos
            if len(error_list) == 0:
                datatype_union[information[0]] = information[1:]
                # y se actualiza el atributo correspondiente
                self.dict_union = datatype_union
            else:
                # en caso contrario, se almacena la lista de errores correspondientes
                self.error_union = error_list
        else:
            # en caso contrario, se almacena la lista con el error correspondiente
            self.error_union = [f"ERROR: {information[0]} ya fue definido como un tipo de datos"]
    
    # funcion para describir un tipo de datos 
    def describir(self, nombre):
        self.descripcion_dato = []
        self.error_descripcion = ""
        # si el nombre a describir se encuenta en algundo de los diccionarios
        if nombre in datatype_struct.keys() or nombre in datatype_union.keys() or nombre in datatype_atomico.keys():
            # se obtiene la descripcion empaquetado
            descripcion_empaquetado = calcular_descripcion_empaquetado(nombre, [0,0,0])
            # se obtiene la descripcion no empaquetado
            (descripcion_no_empaquetado, stack_no_empaquetado) = calcular_descripcion_no_empaquetado(nombre, [0,0,0], [4]*200)
            # se obtiene la descripcion reordenado
            descripcion_reordenado = calcular_descripcion_reordenado(nombre, [0,0,0])
            
            # y se actualiza el atributo correspondiente
            self.descripcion_dato = [descripcion_empaquetado, descripcion_no_empaquetado, descripcion_reordenado]
        else:
            # en caso contrario, se almacena el error correspondiente.
            self.error_descripcion = f"ERROR: {nombre} no ha sido definido como tipo de datos."