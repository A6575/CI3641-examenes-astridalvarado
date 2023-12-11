class ManejadorVtable():
    def __init__(self) -> None:
        self.manejador_vtable = {}
        self.error_atributos = ""
        self.error_clase = ""
        self.error_superclase = ""

    def definir_clase(self, clase, atributos, superclase = None):
        self.error_atributos = ""
        self.error_clase = ""
        self.error_superclase = ""

        metodos_clase = list(map(atributos.count, set(atributos)))
        if any([x for x in metodos_clase if x > 1]):
            self.error_atributos = "ERROR: existen metodos con nombres repetidos en la definicion de la clase"
        if clase in self.manejador_vtable.keys():
            self.error_clase = f"ERROR: la clase {clase} ya existe."
        if superclase != None and superclase not in self.manejador_vtable.keys():
            self.error_superclase = f"ERROR: la superclase {superclase} no existe."
        
        if self.error_atributos == "" and self.error_clase == "" and self.error_superclase == "":
            self.manejador_vtable[clase] = [atributos, superclase]
    
    def describir_clase(self, clase):
        self.error_clase = ""
        metodos_clase = []

        if clase not in self.manejador_vtable.keys():
            self.error_clase = f"la clase {clase} no ha sido definida"
        else:
            vtable_clase = self.manejador_vtable[clase]
            metodos_clase.append([set(vtable_clase[0]), clase])

            while vtable_clase[1] != None:
                superclase = vtable_clase[1]
                vtable_clase = self.manejador_vtable[superclase]
                conjuntos_metodos_clase = [set(metodos[0]) for metodos in metodos_clase]
                conjunto_metodos_actual = set(vtable_clase[0])

                for u_metodos in conjuntos_metodos_clase:
                    if any(u_metodos & conjunto_metodos_actual):
                        conjunto_metodos_actual -= u_metodos

                metodos_clase.append([conjunto_metodos_actual, superclase])
                
        return metodos_clase