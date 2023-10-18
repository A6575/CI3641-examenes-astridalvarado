LOCAL_MACHINE = "LOCAL"

traductores = {}
interpretes = {}
programas = {}
maquinas_creadas = []

def can_execute(name, last_language):
    list_of_language = programas.keys()
    language = ""

    for languages in list_of_language:
        if name in programas[languages]["creados"]:
            language = languages
            break
    
    if last_language != language and programas.get(last_language) is not None and name in programas[last_language]["creados"]:
        language = last_language
    
    if language == "":
        print(f"El archivo '{name}' no ha sido definido en ningun lenguaje actual.")
    elif language in maquinas_creadas or language == LOCAL_MACHINE:
        print(f"Es posible ejecutar '{name}' en {language}")
    else:
        execute = False
        maquinas_creadas.insert(0, LOCAL_MACHINE)
        for machine in maquinas_creadas:
            for programs in list_of_language:
                if "traducidos" in programas[programs]:
                    for traducLanguage in programas[programs]["traducidos"]:

                        if machine == traducLanguage[1] and name in traducLanguage[0]:
                            if machine == LOCAL_MACHINE:
                                print(f"Es posible ejecutar '{name}' en {language}")
                                execute = True
                                break
                        
                            if traductores.get(machine) is None:
                                continue

                            if language in traductores[machine][programs]:  
                                print(f"Es posible ejecutar '{name}' en {language}")
                                execute = True
                                break
                if execute:
                    break
            if execute:
                break
        maquinas_creadas.remove(LOCAL_MACHINE)
        if not execute:
            print(f"No es posible ejecutar '{name}' en {language}")

def can_be_new_trac(base, type):
    if base in maquinas_creadas:
        list_of_base_language = traductores[base].copy().keys()
        for origins in list_of_base_language:
            if origins in traductores:
                destination_languages = traductores[base][origins]
                for dest in destination_languages:
                    if dest not in traductores:
                        traductores.update({dest : traductores[origins]})
                    else:
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
        if type == 1:
            for machine in maquinas_creadas:
                if traductores.get(machine) is not None and base in traductores[machine]:
                    for origin in traductores[base].keys():
                        if origin not in traductores[machine]:
                            traductores[machine].update(traductores[base])
                        else:
                            traductores[machine][origin].extend(traductores[base][origin])
        else:
            for machine in maquinas_creadas:

                if traductores.get(machine) is not None and base in traductores[machine]:
                    for origin in traductores[machine][base]:
                        if origin not in interpretes:
                            interpretes.update({ origin : traductores[machine][base] })
                        else:
                            for interOrigin in interpretes[origin]:
                                if interpretes[origin].count(interOrigin) != 0:
                                    continue
                                interpretes[origin].append(interOrigin)

def actualizar():
    programming_language = programas.keys()
    for machine in maquinas_creadas:
        if machine in interpretes:
            list_of_inter = interpretes[machine]
            for intr in list_of_inter:
                if maquinas_creadas.count(intr) != 0:
                    continue
                maquinas_creadas.extend(interpretes[machine])
        
        if machine in traductores:
            can_be_new_trac(machine,0)

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
                            programas[language]["traducidos"].append([[[name], newLan]])
    print(f"Se definio el programa '{name}', ejecutable en {language}")