# VARIABLE GLOBAL PARA REPRESENTAR LA MAQUINA GLOBAL DE LA SIMULACION
LOCAL_MACHINE = "LOCAL"

traductores = {}        # Diccionarios para representar los traductores. Ejemplo: para un traductor escrito en A, que va de B a C,
                        # una instacia para este diccionario seria {"A":{"B":["C"]}}

interpretes = {}        # Diccionario para reoresentar interpretadores. Ejemplo: para un interprete escrito en A que ejecuta B,
                        # una instancia para este diccionario seria {"A": ["B"]}

programas = {}          # Diccionario para representar programas. Ejemplo: para un programa 'p1' escrito en A y este puede ser traducido a B,
                        # se tiene que {"A":{"creados": ["p1"], "traducidos":[ [ ["p1"], "B" ] ]}}

maquinas_creadas = []   # Lista de maquinas creadas   

# Funcion que, dado el nombre del archivo y el ultimo programa seleccionado, 
# indica si puede ser ejecutada o no
def can_execute(name, last_language):
    list_of_language = programas.keys()     # se obtiene la lista de lenguajes en donde se han escrito los programas
    language = ""                           # variable para guardar el lenguaje del programa

    # Se busca el nombre por todos los programas creados y se obtiene su lenguaje
    for languages in list_of_language:
        if name in programas[languages]["creados"]:
            language = languages
            break
    
    # en caso de que el ultimo lenguaje seleccionado no sea igual al conseguido, que ademas pertenezca a los lenguajes escritos
    # y el archivo haya sido creado para este ultimo lenguaje, se cambia. Esto es para poder determinar, en caso de tener lenguajes
    # que comparten nombres de archivos, que se pregunta si es posible ejecutar el archivo ultimo seleccionado.
    if last_language != language and programas.get(last_language) is not None and name in programas[last_language]["creados"]:
        language = last_language
    
    # si no se consigue lenguaje, quiere decir que no ha sido declarado ningun archivo con ese nombre y por lo tanto se reporta
    # el mensaje correspondiente
    if language == "":
        return (f"El archivo '{name}' no ha sido definido en ningun lenguaje actual.")
    elif language in maquinas_creadas or language == LOCAL_MACHINE:
        # si el lenguaje esta en las maquinas creadas o es la maquina local indicamos que es posible ejecutar
        return (f"Es posible ejecutar '{name}' en {language}")
    else:
        # en otro caso, buscamos para todas las maquinas existentes una posible traduccion que permita ejecutar el programa
        maquinas_creadas.insert(0, LOCAL_MACHINE)
        for machine in maquinas_creadas:
            for programs in list_of_language:
                if "traducidos" in programas[programs]:
                    for traducLanguage in programas[programs]["traducidos"]:

                        if machine == traducLanguage[1] and name in traducLanguage[0]:
                            if machine == LOCAL_MACHINE:
                                return (f"Es posible ejecutar '{name}' en {language}")
                        
                            for traducLan in traductores.keys():
                                if (traductores[traducLan].get(programs) is not None and 
                                    traducLanguage[1] in traductores[traducLan][programs] and 
                                    traducLan in maquinas_creadas):
                                    return (f"Es posible ejecutar '{name}' en {language}")
                            
                            if traductores.get(machine) is None:
                                continue

                            if traductores[machine].get(programs) is not None and language in traductores[machine][programs]:  
                                return (f"Es posible ejecutar '{name}' en {language}")

        maquinas_creadas.remove(LOCAL_MACHINE)
        # en caso de no encontrar nada, se indica al usuario
        return (f"No es posible ejecutar '{name}' en {language}")

# Funcion para saber si es posible realizar una traduccion inmediata dada un lenguaje base y un tipo.
# El tipo permite distinguir la busqueda entre interprete (0) y traductor (1)
def can_be_new_trac(base, type):
    # se verifica que mi leguaje base ya posea una maquina, y en ese caso
    if base in maquinas_creadas:
        list_of_base_language = traductores[base].copy().keys()
        
        # se itera por los lenguajes origenes de dicha base
        for origins in list_of_base_language:
            # y si se encuentra como lenguaje base de los traductores, quiere decir que 
            # es posible crear un nuevo traductor a partir de una traduccion. 
            if origins in traductores:
                destination_languages = traductores[base][origins]
                for dest in destination_languages:
                    if dest not in traductores:
                        traductores.update({dest : traductores[origins]})
                    else:
                        # Si la base del nuevo traductor ya pertecia los traductores, entonces se agrega el nuevo en el
                        # diccionario interno
                        origins_languages = traductores[origins].keys()
                        for newOring in origins_languages:
                            if newOring not in traductores[dest]:
                                traductores[dest].update(traductores[origins])
                            else:
                                for destiny in traductores[dest][newOring]:
                                    if traductores[dest][newOring].count(destiny) != 0:
                                        continue
                                    traductores[dest][newOring].append(destiny)
    else:
        # en caso de que nuestra base no posea una maquina y sea de tipo 1, se itera por las maquinas 
        # actuales en busca de generar nuevos traductores utilizando el traductor actual
        if type == 1:
            for machine in maquinas_creadas:
                if traductores.get(machine) is not None and base in traductores[machine]:
                    for origin in traductores[base].keys():
                        if origin not in traductores[machine]:
                            traductores[machine].update(traductores[base])
                        else:
                            traductores[machine][origin].extend(traductores[base][origin])
        else:
            # por otro lado, si nuestra base no tiene maquina creadas pero es de tipo 0, entonces
            # buscamos gernerar nuevos interpretes a partir de nuestro traductor actual
            for machine in maquinas_creadas:
                if traductores.get(machine) is not None and base in traductores[machine]:
                    for origin in traductores[machine][base]:
                        if origin not in interpretes:
                            interpretes.update({ origin : interpretes[base] })
                        else:
                            for interOrigin in interpretes[origin]:
                                if interpretes[origin].count(interOrigin) != 0:
                                    continue
                                interpretes[origin].append(interOrigin)

# Funcion actualizar, esta es llamada cada vez que se crea un nuevo interpretes o traductores
# en busca de realizar nuevas todas las posible traducciones de interpretes, programas y traductores
def actualizar():
    programming_language = programas.keys()
    interperters_base_language = interpretes.copy().keys()
    maquinas_creadas.insert(0, LOCAL_MACHINE)
    
    # se itera por las maquinas creadas
    for machine in maquinas_creadas:
        # si hay un interprete con lenguaje base ejecutable en alguna maquina
        # entonces se realiza su traduccion
        if machine in interpretes:
            list_of_inter = interpretes[machine]
            for intr in list_of_inter:
                if maquinas_creadas.count(intr) != 0:
                    continue
                maquinas_creadas.extend(interpretes[machine])
        
        # si ademas existe alguno traductor con escrito en algun lenguaje que se pueda
        # ejecutar en alguna maquina creada
        if machine in traductores:
            # se vueleve a llamar a la funcion que realiza traducciones
            can_be_new_trac(machine,1)
            
            # Ademas, se itera por todos los lenguajes en los cuales tenemos archivos escritos
            # para poder realizar traducciones nuevas
            for language in programming_language:
                if traductores[machine].get(language) is None:
                    continue

                for newLan in traductores[machine][language]:
                    if "traducidos" not in programas[language]:
                        programas[language].update({"traducidos" : [[programas[language]["creados"], newLan]]})
                    else:

                        for traduc in programas[language]["traducidos"]:
                            if traduc[1] == newLan:
                                for name in programas[language]["creados"]:
                                    if traduc[0].count(name) != 0:
                                        continue
                                    traduc[0].append(name)
                            else:
                                programas[language]["traducidos"].append([programas[language]["creados"], newLan])
            
            # por otro lado, se busca crear nuevos interpretadores mediante traducciones
            for baseLan in interperters_base_language:
                if traductores[machine].get(baseLan) is None:
                    continue

                for newLan in traductores[machine][baseLan]:
                    if newLan not in interpretes:
                        interpretes.update({newLan: interpretes[baseLan]})
                    else:
                        for interOrigin in interpretes[newLan]:
                            if interpretes[newLan].count(interOrigin) != 0:
                                continue
                            interpretes[newLan].append(interOrigin)

    maquinas_creadas.remove(LOCAL_MACHINE)

# Funcion que, dado un lenguaje que ademas posee traducciones, actualiza cada programa
# para conseguir mas traducciones de programas
def actualizar_programas(language):
    maquinas_creadas.insert(0, LOCAL_MACHINE)
    programas_a_actualizar = programas[language]["traducidos"]
    for program in programas_a_actualizar:
        for machine in maquinas_creadas:
            if machine in traductores and traductores[machine].get(program[1]) is not None:
                for tranlations in traductores[machine][program[1]]:
                    if tranlations != program[1]:
                        programas[language]["traducidos"].append([ program[0] , tranlations ])
    maquinas_creadas.remove(LOCAL_MACHINE)

# Funcion para agregar traductores al diccionario correspondiente
def add_trac(base, origin, dest):
    if base in traductores:
        if origin in traductores[base]:
            traductores[base].get(origin).append(dest)
        else:
            traductores[base].update({origin : [dest]})    
    else:
        traductores.update({base : dict([(origin, [dest])])})
    
    can_be_new_trac(base, 1)
    actualizar()
    print(f"Se definio un traductor de {origin} hacia {dest}, escrito en {base}")

# Funcion para agregar iterpretes al diccionanrio correspondiente
def add_inter(base, language):
    if base in interpretes:
        interpretes[base].append(language)
    else:
        interpretes.update({base : [language]})
    
    if base.upper() == LOCAL_MACHINE or base in maquinas_creadas:
        maquinas_creadas.append(language)
    
    can_be_new_trac(base, 0)
    actualizar()
    print(f"Se definio un interprete para {language}, escrito en {base}")

# Funcion para agregar programas al diccionario correspondiente y traducciones inmediatas de este
def add_program(name, language):
    if language in programas:
        if name in programas[language]["creados"]:
            print(f"ERROR: El programa {name} ya fue escrito en {language}")
        else:
            programas[language]["creados"].append(name)
    else:
        programas.update({language : {"creados" : [name]}})
    
    for machine in maquinas_creadas:
        if traductores.get(machine) is not None and language in traductores[machine]:
            for newLan in traductores[machine][language]:
                if "traducidos" not in programas[language]:
                    programas[language].update({"traducidos" : [[[name], newLan]]})
                else:
                    for traduc in programas[language]["traducidos"]:
                        if traduc[1] == newLan:
                            if traduc[0].count(name) != 0:
                                continue
                            traduc[0].append(name)
                        else:
                            programas[language]["traducidos"].append([[name], newLan])
    
    if programas[language].get("traducidos") is not None:
        actualizar_programas(language)
    print(f"Se definio el programa '{name}', ejecutable en {language}")