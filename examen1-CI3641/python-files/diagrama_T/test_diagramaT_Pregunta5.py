from diagramaT import *

def test_Parcial ():
    add_program("fibonacci", "LOCAL")
    assert(programas == {"LOCAL":{"creados":["fibonacci"]}} and
           can_execute("fibonacci", "LOCAL") == "Es posible ejecutar 'fibonacci' en LOCAL")
    add_program("factorial", "JAVA")
    assert(programas == {"LOCAL":{"creados":["fibonacci"]}, "JAVA":{"creados":["factorial"]}} and
           can_execute("factorial", "JAVA") == "No es posible ejecutar 'factorial' en JAVA")
    add_inter("C", "JAVA")
    assert(interpretes == {"C":["JAVA"]})
    add_trac("C", "JAVA", "C")
    assert(traductores == {"C":{"JAVA":["C"]}} and
           can_execute("factorial", "JAVA") == "No es posible ejecutar 'factorial' en JAVA")
    add_inter("LOCAL", "C")
    assert(interpretes == {"C":["JAVA"], "LOCAL":["C"]} and
           maquinas_creadas == ["C", "JAVA"] and
           programas == {"LOCAL":{"creados":["fibonacci"]}, "JAVA":{"creados":["factorial"], "traducidos": [[["factorial"], "C"]]}} and
           can_execute("factorial", "JAVA") == "Es posible ejecutar 'factorial' en JAVA")
    add_program("holamundo", "Python3")
    assert(programas == {"LOCAL":{"creados":["fibonacci"]}, "JAVA":{"creados":["factorial"], "traducidos": [[["factorial"], "C"]]}, "Python3":{"creados":["holamundo"]}} and
           can_execute("factorial", "JAVA") == "Es posible ejecutar 'factorial' en JAVA")
    add_trac("wtf42", "Python3", "LOCAL")
    assert(traductores == {"C":{"JAVA":["C"]}, "wtf42":{"Python3":["LOCAL"]}} and
           can_execute("holamundo", "Python3") == "No es posible ejecutar 'holamundo' en Python3")
    add_trac("C", "wtf42", "JAVA")
    assert(traductores == {"C":{"JAVA":["C"], "wtf42":["JAVA"], "Python3":["LOCAL"]}, "wtf42":{"Python3":["LOCAL"]}, "JAVA":{"Python3":["LOCAL"]}} and
           programas == {"LOCAL":{"creados":["fibonacci"]}, "JAVA":{"creados":["factorial"], "traducidos": [[["factorial"], "C"]]}, "Python3":{"creados":["holamundo"], "traducidos":[[["holamundo"], "LOCAL"]]}} and
           can_execute("holamundo", "Python3") == "Es posible ejecutar 'holamundo' en Python3")