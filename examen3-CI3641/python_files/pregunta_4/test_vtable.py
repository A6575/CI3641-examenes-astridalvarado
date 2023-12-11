from vtable import *

def test_definir_clase():
    manejador_global = ManejadorVtable()
    manejador_global.definir_clase("A", ["f", "g"])
    
    assert("A" in manejador_global.manejador_vtable.keys() and
           manejador_global.manejador_vtable["A"] == [["f", "g"], None])
    
    manejador_global.definir_clase("B", ["f", "h"], "A")

    assert("B" in manejador_global.manejador_vtable.keys() and
           manejador_global.manejador_vtable["B"] == [["f", "h"], "A"])

def test_describir_clase():
    manejador_global = ManejadorVtable()
    manejador_global.definir_clase("A", ["f", "g"])
    metodos_clase  = manejador_global.describir_clase("A")

    assert(metodos_clase == [[{"f", "g"}, "A"]])
    
    manejador_global.definir_clase("B", ["f", "h"], "A")
    metodos_clase  = manejador_global.describir_clase("B")

    assert(metodos_clase == [[{"f", "h"}, "B"], [{"g"}, "A"]])

    manejador_global.definir_clase("C", ["a", "b", "c", "d"], "B")
    metodos_clase  = manejador_global.describir_clase("C")

    assert(metodos_clase == [[{"a","b","c","d"}, "C"], [{"f","h"}, "B"], [{"g"}, "A"]])

    manejador_global.definir_clase("D", ["a", "f", "e", "g"], "C")
    metodos_clase  = manejador_global.describir_clase("D")

    assert(metodos_clase == [[{"a", "f", "e", "g"}, "D"], [{"b","d","c"}, "C"], [{"h"}, "B"], [set(), "A"]])

def test_errores():
    manejador_global = ManejadorVtable()
    manejador_global.definir_clase("A", ["f", "g"])

    assert(manejador_global.error_atributos == "" and manejador_global.error_clase == "" and manejador_global.error_superclase == "")

    manejador_global.definir_clase("A", ["f","f","f"], "C")

    assert(manejador_global.error_atributos != "" and manejador_global.error_clase != "" and manejador_global.error_superclase != "")

    manejador_global.describir_clase("D")
    
    assert(manejador_global.error_clase != "")

