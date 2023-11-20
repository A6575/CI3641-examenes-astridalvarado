from aritmetica import *

def test_aritmetica_init ():
    expr = Expresion("+ * + 3 4 5 7")
    assert(expr.expression == "+ * + 3 4 5 7" and expr.expression_as_list == ["+","*","+",3,4,5,7] and expr.infix_expression_as_list == ["+","*","+","3","4","5","7"])

def test_aritmetica_eval_pre ():
    expr = Expresion("+ * + 3 4 5 7")
    expr.eval("PRE")
    assert(expr.stack[0] == 42)
    expr = Expresion("- + 4 2 * 3 / 6 6")
    expr.eval("PRE")
    assert(expr.stack[0] == 3)

def test_aritmetica_eval_post ():
    expr = Expresion("8 3 - 8 4 4 + * +")
    expr.eval("POST")
    assert(expr.stack[0] == 69)
    expr = Expresion("4 2 + 3 6 6 / * -")
    expr.eval("POST")
    assert(expr.stack[0] == 3)

def test_aritmetica_mostrar_pre ():
    expr = Expresion("+ * + 3 4 5 7")
    expr.mostrar("PRE")
    assert(expr.infix_stack[0] == "(3 + 4) * 5 + 7")
    expr = Expresion("- + 4 2 * 3 / 6 6")
    expr.mostrar("PRE")
    assert(expr.infix_stack[0] == "4 + 2 - 3 * 6 / 6")

def test_aritmetica_mostrar_post ():
    expr = Expresion("8 3 - 8 4 4 + * +")
    expr.mostrar("POST")
    assert(expr.infix_stack[0] == "8 - 3 + 8 * (4 + 4)")
    expr = Expresion("4 2 + 3 6 6 / * -")
    expr.mostrar("POST")
    assert(expr.infix_stack[0] == "4 + 2 - 3 * 6 / 6")

def test_aritmetica_es_Expresion ():
    assert(es_Expresion("4") and es_Expresion("+") and not es_Expresion("&") and not es_Expresion("A"))