module Conjunto where

-- Definicion de tipo Conjunto a
type Conjunto a = a -> Bool

-- a) Dado Conjunto a, devuelve un booleano que indica si cumple con la funcion 'a->Bool'
--    y de esta forma se verifica que el elemento pertenezca al conjunto
miembro :: Conjunto a -> a -> Bool
miembro conjunto = conjunto 

-- b) Para cualquier entrada, se tiene que el conjunto vacio es aquella funcion que siempre retorna False
vacio :: Conjunto a
vacio _ = False 

-- c) Dado un elemento, se crea el conjunto {a}. Para esto, se utiliza la equivalencia y de esta forma
--    verificar que el elemento siempre sea el mismo
singleton :: (Eq a) => a -> Conjunto a
singleton elemento1 elemento2 = elemento1 == elemento2

-- d) Dada una lista, se crea un Conjunto a verificando siempre que el elemento pertenezca a la lista dada
desdeLista :: (Eq a) => [a] -> Conjunto a
desdeLista lista elemento = elemento `elem` lista 

-- e) Dado un Conjunto a, se devuelve otro Conjunto a tal que no cumpla con la funcion 'a->Bool' inicial
complemento :: Conjunto a -> Conjunto a
complemento conjunto elemento = not (conjunto elemento)

-- f) Dado dos Conjunto a, retorna un Conjunto a tal que satisfagan uno o ambos Conjunto a pasados como 
--    argumento 
union :: Conjunto a -> Conjunto a -> Conjunto a
union conjunto1 conjunto2 elemento = conjunto1 elemento || conjunto2 elemento

-- g) Dado dos Conjunto a, retorna un Conjunto a tal que satisfagan exactamente ambos Conjunto a pasados como
--    argumento
interseccion :: Conjunto a -> Conjunto a -> Conjunto a
interseccion conjunto1 conjunto2 elemento = conjunto1 elemento && conjunto2 elemento

-- h) Dado dos Conjunto a, retorna un Conjunto a tal que cumplan con el primer Conjunto a pero no con el segundo
diferencia :: Conjunto a -> Conjunto a -> Conjunto a
diferencia conjunto1 conjunto2 elemento = conjunto1 elemento && not (conjunto2 elemento)

-- i) Dado una funcion f 'b->a' y un Conjunto a, retorna un Conjunto b tal que al aplicar f a los elementos del 
--    Conjunto b, pertenezcan al Conjunto a
transformar :: (b -> a) -> Conjunto a -> Conjunto b
transformar transformacion conjunto1 elemento = miembro conjunto1 $ transformacion elemento