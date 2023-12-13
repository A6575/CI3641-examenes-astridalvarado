# Clase para manejas la tablas vituales de metodos
class ManejadorVtable():
    # construcctor de la clase 
    def __init__(self) -> None:
        self.manejador_vtable = {}      # diccionario donde se almacenaran las clases y sus metodos
        self.error_atributos = ""       # mensaje de error correspondiente a los atributdos de las clases
        self.error_clase = ""           # mensaje de error correspondiente a la clase
        self.error_superclase = ""      # mensaje de error correspondiente a la superclase

    # funcion para definir nuevas clases 
    def definir_clase(self, clase: str, atributos: list, superclase: str = None):
        # limpiar mensajes de error
        self.error_atributos = ""
        self.error_clase = ""
        self.error_superclase = ""

        # validar atributos para que no existan nombres repetidos
        metodos_clase = list(map(atributos.count, set(atributos)))
        if any([x for x in metodos_clase if x > 1]):
            self.error_atributos = "ERROR: existen metodos con nombres repetidos en la definicion de la clase"
        # verificar que una clase ya existente no pueda ser redefinida
        if clase in self.manejador_vtable.keys():
            self.error_clase = f"ERROR: la clase {clase} ya existe."
        # verificar que la superclase exista
        if superclase != None and superclase not in self.manejador_vtable.keys():
            self.error_superclase = f"ERROR: la superclase {superclase} no existe."
        
        # si no se encontró ningún error, se almacena la clase en el diccionario
        if self.error_atributos == "" and self.error_clase == "" and self.error_superclase == "":
            self.manejador_vtable[clase] = [atributos, superclase]
    
    def describir_clase(self, clase: str):
        self.error_clase = ""   # limpiar mensaje de error
        metodos_clase = []      # lista donde se almacenaran los metodos de la clase

        # validar que la clase exista
        if clase not in self.manejador_vtable.keys():
            self.error_clase = f"la clase {clase} no ha sido definida"
        else:
            # obtener los metodos de la clase y sus superclases, de tenerlas
            vtable_clase = self.manejador_vtable[clase]
            # se agrega a la lista los metodos de la clase como un conjunto, y la clase de donde se obtuvo
            metodos_clase.append([set(vtable_clase[0]), clase])

            # mientras que la superclase no sea None
            while vtable_clase[1] != None:
                # se obtiene el nombre de la superclase
                superclase = vtable_clase[1]
                # se obtiene los metodos de la superclase
                vtable_clase = self.manejador_vtable[superclase]
                # se realiza una transformacion de los metodos encontrados en la lista metodos_clase
                conjuntos_metodos_clase = [set(metodos[0]) for metodos in metodos_clase]
                # se obtiene el conjunto de metodos de la superclase
                conjunto_metodos_actual = set(vtable_clase[0])

                # y para todos los conjuntos de los metodos de la clase
                for u_metodos in conjuntos_metodos_clase:
                    # siempre que exista intersección, se realiza la diferencia de conjuntos
                    if any(u_metodos & conjunto_metodos_actual):
                        conjunto_metodos_actual -= u_metodos
                
                # finalmente, se agrega a la lista
                metodos_clase.append([conjunto_metodos_actual, superclase])
                
        return metodos_clase