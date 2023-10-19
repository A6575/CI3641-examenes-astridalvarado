from diagramaT import *

def test_add_trac():
    add_trac("C", "HASKELL", "C")
    assert(traductores == {"C":{"HASKELL":["C"]}})
    add_trac("LOCAL", "C", "PYTHON")
    assert(traductores == {"C":{"HASKELL":["C"]}, "LOCAL": {"C":["PYTHON"]}, "PYTHON":{"HASKELL":["C"]}})
    add_trac("PYTHON3", "JAVASCRIPT", "RUBY")
    assert(traductores == {"C":{"HASKELL":["C"]}, "LOCAL": {"C":["PYTHON"]}, "PYTHON":{"HASKELL":["C"]}, "PYTHON3":{"JAVASCRIPT":["RUBY"]}})
    add_trac("PYTHON3", "JAVASCRIPT", "HTML")
    assert(traductores == {"C":{"HASKELL":["C"]}, "LOCAL": {"C":["PYTHON"]}, "PYTHON":{"HASKELL":["C"]}, "PYTHON3": {"JAVASCRIPT":["RUBY", "HTML"]}})
    add_trac("PYTHON3", "KOTLIN", "HTML")
    assert(traductores == {"C":{"HASKELL":["C"]}, "LOCAL": {"C":["PYTHON"]}, "PYTHON":{"HASKELL":["C"]}, "PYTHON3": {"JAVASCRIPT":["RUBY", "HTML"], "KOTLIN":["HTML"]}})

def test_add_inter():
    add_inter("LOCAL", "C")
    assert(interpretes == {"LOCAL":["C"]} and maquinas_creadas == ["C"])
    add_inter("HASKELL", "JAVA")
    assert(interpretes == {"LOCAL":["C"], "HASKELL":["JAVA"], "C":["JAVA"], "PYTHON":["JAVA"]} and maquinas_creadas == ["C", "JAVA"])

def test_add_program():
    add_program("holamundo", "LOCAL")
    assert(programas == {"LOCAL":{"creados":["holamundo"]}})
    add_program("new_holamundo", "JAVA")
    assert(programas == {"LOCAL":{"creados":["holamundo"]}, "JAVA":{"creados":["new_holamundo"]}})
    add_program("myProgram","HASKELL")
    assert(programas == {"LOCAL":{"creados":["holamundo"]}, "JAVA":{"creados":["new_holamundo"]}, "HASKELL":{"creados":["myProgram"], "traducidos":[ [["myProgram"], "C"], [["myProgram"], "PYTHON"] ]}})
    add_program("new_holamundo", "JAVA")
    assert(programas == {"LOCAL":{"creados":["holamundo"]}, "JAVA":{"creados":["new_holamundo"]}, "HASKELL":{"creados":["myProgram"], "traducidos":[ [["myProgram"], "C"], [["myProgram"], "PYTHON"] ]}})

def test_can_execute():
    assert(can_execute("factorial", "HASKELL") == "El archivo 'factorial' no ha sido definido en ningun lenguaje actual.")
    assert(can_execute("holamundo", "HASKELL") == "Es posible ejecutar 'holamundo' en LOCAL")
    assert(can_execute("new_holamundo", "HASKELL") == "Es posible ejecutar 'new_holamundo' en JAVA")
    assert(can_execute("myProgram", "HASKELL") == "Es posible ejecutar 'myProgram' en HASKELL")
    add_program("program1", "ADA")
    assert(can_execute("program1", "ADA") == "No es posible ejecutar 'program1' en ADA")
