# importacion de la libreria math para el funcionamiento de la clase
import math

# Clase Buddy System
class Buddy_System():
    # Constructor: dado un entero n se crea la lista de bloques,
    # se calcula el logaritmo base 2 (redondeado hacia abajo) del mismo
    # y se crea la lista de bloques libres.
    def __init__(self, n:int) -> None:
        self.block_list = [[n, ""]]
        self.power_of_two = math.floor(math.log2(n))
        self.list_of_free_block = [[2**i, 0] for i in range(self.power_of_two+1)]
    
    # Funcion para mostrar en pantalla el estado del buddy system
    def mostrar(self):
        # Siempre se empieza reseteando la lista de bloques libres 
        self.list_of_free_block = [[2**i, 0] for i in range(self.power_of_two+1)]

        print("\t\t-- ESTADO DE LA SIMULACION --\n")
        
        # Se establece un contador de bloques libres para saber de la cantidad total de estos
        count_of_free_blocks = 0

        # recorremos la lista de bloques totales
        for block in self.block_list:

            # Y para aquellos que posean nombre, se imprime junto a la cantidad de bloques asignados
            if block[1] != "":
                print(f"- {block[1]}: {block[0]} bloques reservados\n")
            else:
                # en caso de encontrarnos con bloques libres, aumentamos el contador total
                count_of_free_blocks += block[0]
                # y se empieza a distribuir en la lista de buddy system
                finding_blocks = block[0]
                while finding_blocks != 0:
                    # Para esto, se calcula el logaritmo base 2 del bloque actual
                    power_two = math.floor(math.log2(finding_blocks))
                    # E iterando por la lista de bloques libres
                    for freeblock in self.list_of_free_block:
                        # Se aumenta el contador de bloques con su pontencia de dos correspondiente
                        if freeblock[0] == 2**power_two:
                            freeblock[1] += 1
                    # finalmente se resta dicho valor del bloque 
                    finding_blocks -= 2**power_two 
        
        # Impresion de bloques disponibles organizados en segmentos de potencia de 2  
        print(f"\t\t-- BLOQUES LIBRES DIPONIBLES: {count_of_free_blocks} --\n")
        for freeblocks in self.list_of_free_block:
            print(f"| segmentos de tamano {freeblocks[0]} | ---> {freeblocks[1]} bloques disponibles ")
    
    # Funcion para realizar reserva de memoria dado un numero como string y un nombre
    def reservar(self, str, name):
        reserved_amount = int(str)  # cantidad a reservar
        used_name = False           # variable para indicar si un nombre ha sido ya usado
        
        # Si el nombre ya ha sido usado y se encuentra en la lista totales, se indica cambiando a True 
        for block in self.block_list:
            if name == block[1]:
                used_name = True
                
        if used_name:
            # Si el nombre a reservar ya fue usado, se indica error
            print("ERROR: el nombre ingresado tiene ya bloques reservados")
        else:
            # En caso contrario, recorremos la lista de bloques para poder realizar la reserva correspondiente
            for i in range(len(self.block_list)):
                # se verifica que se pueda hacer la reserva viendo si la cantidad de bloques es suficientemente grande
                # y que este disponible
                if self.block_list[i][1] == "" and (reserved_amount <= self.block_list[i][0]):
                    self.block_list.insert(i+1,[self.block_list[i][0]-reserved_amount, ""])
                    self.block_list[i][0] = reserved_amount
                    self.block_list[i][1] = name
                    
                    break
                else:
                    # si hemos iterado por toda la lista y no ha sido hecho la reserva, de indica error
                    if i == len(self.block_list)-1:
                        print(f"ERROR: no existe espacio contiguo suficientemente grande para ser resevar {reserved_amount} bloques")

    # Funcion para liberar el espacio que fue reservado a partir del nombre
    def liberar(self, name):
        exist_name = False      #variable que indica si el nombre ya existe
        index = 0               # contador del indice para recorrer el arreglo

        # se recorre la lista de bloques en busca de alguna coincidencia de nombre
        # y se almacena el indice de este
        for block in self.block_list:
            if block[1] == name:
                exist_name = True
                index = self.block_list.index(block)
                break
        
        # si el nombre no existe, se reporta error
        if not exist_name:
            print("ERROR: el nombre ingresado no se encuentra como reservado")
        else:
            # En caso contrario, se libera el bloque al borrar el nombre del mismo
            self.block_list[index][1] = ""
            # se inicia el indice en 1
            index = 1
            # y se recorre la lista de bloques en busca de bloques contiguos disponibles
            # para asi obtener el tamano total de bloques contiguos
            while index != len(self.block_list):
                if self.block_list[index-1][1] == "" and self.block_list[index][1] == "":
                    self.block_list[index-1][0] += self.block_list[index][0]
                    del self.block_list[index]
                else:
                    index+=1