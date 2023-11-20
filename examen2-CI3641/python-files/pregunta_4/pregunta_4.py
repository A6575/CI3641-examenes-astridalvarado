# libreria para medir el tiempo de ejecucion
import time
import csv

# Variables globales
ALPHA = 5                   # ((X + Y) mod 5) + 3, para X = 9 y Y = 3
BETA = 4                    # ((Y + Z) mod 5) + 3, para Y = 3 y Z = 8
ALPHA_X_BETA = ALPHA*BETA   # 20

# a) FUNCION RECURSIVA
def F54_recursiva (n:int):
    if n >= 0 and n < ALPHA_X_BETA:
        return n
    elif n >= ALPHA_X_BETA:
        return F54_recursiva(n-4) + F54_recursiva(n-8) + F54_recursiva(n-12) + F54_recursiva(n-16) + F54_recursiva(n-20)
    else:
        return "no se admiten numeros negativos"

# b) FUNCION RECURSION DE COLA
def F54_recursiva_cola(n:int,
                       it = ALPHA_X_BETA,
                       result = 0,
                       aux16 = 0, aux12 = 0, aux8 = 0, aux4 = 0, aux0 = 0,
                       paso16 = 1, paso12 = 1, paso8 = 1, paso4 = 1, paso0 = 1,
                       f54_16 = 16, f54_12 = 12, f54_8 = 8, f54_4 = 4, f54_0 = 0):
    
    if n < 0:
        return "no se admiten numeros negativos"

    # Caso base de la funcion F_5,4
    if n >= 0 and n < ALPHA_X_BETA:
        return n
    
    # Caso base para la funcion recursiva de cola. El resultado se devuelve para 
    # cuando el iterador sea igual a n+1
    if it == n+1:
        return result
    
    # Note que para los casos en los que it (it+1) mod BETA sea 0, quiere decir que 
    # estamos a una iteracion de pasar a los casos multiplos de BETA, por lo que es
    # necesario actualizar 
    if (it+1) % BETA == 0:

        # se aumenta el valor de f54_0 con su paso correspondiente
        f54_0+=paso0
        if f54_0 > ALPHA_X_BETA-1:
            # si dicho valor es mayor o igual a 20, se debe actualizar dicho valor a partir
            # de los valores almacenados anteriormente
            f54_0 = aux0 + aux4 + aux8 + aux12 + aux16

        # se aumenta el valor de f54_4 con su paso correspondiente
        f54_4+=paso4
        if f54_4 > ALPHA_X_BETA-1:
            # si dicho valor es mayor o igual a 20, se debe actualizar dicho valor a partir
            # de los valores almacenados ademas de lo acumulado en f54_0
            f54_4 = f54_0 + aux4 + aux8 + aux12 + aux16
        
        # se aumenta el valor de f54_8 con su paso correspondiente
        f54_8+=paso8
        if f54_8 > ALPHA_X_BETA-1:
            # si dicho valor es mayor o igual a 20, se debe actualizar dicho valor a partir
            # de los valores almacenados ademas de lo acumulado en f54_0 y f54_4
            f54_8 = f54_0 + f54_4 + aux8 + aux12 + aux16
        
        # se aumenta el valor de f54_12 con su paso correspondiente
        f54_12+=paso12
        if f54_12 > ALPHA_X_BETA-1:
            # si dicho valor es mayor o igual a 20, se debe actualizar dicho valor a partir
            # de los valores almacenados ademas de lo acumulado en f54_0, f54_4 y f54_8
            f54_12 = f54_0 + f54_4 + f54_8 + aux12 + aux16
        
        # se aumenta el valor de f54_16 con su paso correspondiente
        f54_16+=paso16
        if f54_16 > ALPHA_X_BETA-1:
            # si dicho valor es mayor o igual a 20, se debe actualizar dicho valor a partir
            # de los valores almacenados ademas de lo acumulado en f54_0, f54_4, f54_8 y f54_12
            f54_16 = f54_0 + f54_4 + f54_8 + f54_12 + aux16
        
        # se actualiza el nuevo paso para la siguiente llamada
        nuevo_paso16 = paso16 + paso12 + paso8 + paso4 + paso0
        
        # se llama de forma recursiva la cola aumentando el iterador, y realizando el intercambio correspondiente
        # de los auxiliares y los pasos
        return F54_recursiva_cola(n, it+1, result,
                                  f54_0, aux16, aux12, aux8, aux4, 
                                  nuevo_paso16, paso16, paso12, paso8, paso4,
                                  f54_16, f54_12, f54_8, f54_4, f54_0)
    else:
        # Se actualiza el resultado con la suma de todos los componentes
        result = f54_16+f54_12+f54_8+f54_4+f54_0
        
        # Y se llama de forma recursiva a la funcion aumentando el iterador y aumentando los componentes con los
        # pasos correspondientes
        return F54_recursiva_cola(n, it+1, result,
                                  aux16, aux12, aux8, aux4,aux0,
                                  paso16, paso12, paso8, paso4,paso0,
                                  f54_16+paso16, f54_12+paso12, f54_8+paso8, f54_4+paso4, f54_0+paso0)

# c) FUNCION ITERATIVA
def F54_iterativa (n:int):
    # Se inicializa f54 como una lista de tamano n+1 con todos sus valores en 0
    f54 = [0] * (n+1)
    
    if n < 0:
        return "no se admiten numeros negativos"
    
    # iteramos por los numeros de 0 hasta n
    for i in range(n+1):
        # caso base para la funcion, almacenando el valor en la lista creada
        if i >= 0 and i < ALPHA_X_BETA:
            f54[i] = i
        else:
            # se almacena para i >= 20 como la suma de los elementos en los f54 cada 4 pasos
            f54[i] = f54[i-4] + f54[i-8] + f54[i-12] + f54[i-16] + f54[i-20]
    
    # finalmente se retorna el valor en la posicion n
    return f54[n]

# funcion para obtener la media del tiempo de ejecucion de cada programa y posteriormente dichos 
# valores exportarlos en un archivo csv
def generate_csv(test_case:[[int]]):
    values = []
    headers = ["N", "Funcion Recursiva", "Funcion Recursiva de Cola", "Funcion Iterativa"]
    for test in test_case:
        meantime1 = 0
        meantime2 = 0
        meantime3 = 0
        dict_tmp = {}

        dict_tmp["N"] = test[0]
        
        for n in test:
            init = time.perf_counter()
            F54_recursiva(n)
            end = time.perf_counter()
            meantime1 += (end-init)
    
            init = time.perf_counter()
            F54_recursiva_cola(n)
            end = time.perf_counter()
            meantime2 += (end-init)
    
            init = time.perf_counter()
            F54_iterativa(n)
            end = time.perf_counter()
            meantime3 += (end-init)
        
        dict_tmp["Funcion Recursiva"] = float(f"{(meantime1/10):0.4f}")
        dict_tmp["Funcion Recursiva de Cola"] = float(f"{(meantime2/10):0.4f}")
        dict_tmp["Funcion Iterativa"] = float(f"{(meantime3/10):0.4f}")
        
        values.append(dict_tmp)
    
    with open('values.csv', mode='w') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames=headers )
        writer.writeheader()

        for val in values:
            writer.writerow(val)

# funcion principal 
def main():
    N = int(input("Ingrese un numero no negativo: "))
    
    print("Para F_5,4 de forma RECURSIVA")
    init = time.perf_counter()
    val_recursivo = F54_recursiva(N)
    end = time.perf_counter()
    
    total_time = end - init
    print(f"\t>> Valor obtenido: {val_recursivo}")
    print(f"\t>> El tiempo transcurrido es de: {total_time:0.4f} segundos")

    print("Para F_5,4 de forma RECURSIVA DE COLA")
    init = time.perf_counter()
    val_recursivo = F54_recursiva_cola(N)
    end = time.perf_counter()
    
    total_time = end - init
    print(f"\t>> Valor obtenido: {val_recursivo}")
    print(f"\t>> El tiempo transcurrido es de: {total_time:0.4f} segundos")

    print("Para F_5,4 de forma ITERATIVA")
    init = time.perf_counter()
    val_recursivo = F54_iterativa(N)
    end = time.perf_counter()
    
    total_time = end - init
    print(f"\t>> Valor obtenido: {val_recursivo}")
    print(f"\t>> El tiempo transcurrido es de: {total_time:0.4f} segundos")

    # Si desea obtener la media de estos casos de prueba en archivo csv, descomente la funcion.
    #generate_csv([[20]*10,[40]*10,[60]*10,[70]*10,[80]*10,[90]*10,[100]*10,[110]*10,[120]*10])

if __name__ == "__main__":
    main()