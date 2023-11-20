module ArbolMB where
import Data.Maybe 

-- tipo de datos ArbolMB
data ArbolMB a = Vacio
                | RamaM a (ArbolMB a)
                | RamaB a (ArbolMB a) (ArbolMB a)
                deriving Show
-- a)
-- Vacio :: ArbolMB a
-- RamaM :: a -> ArbolMB a -> ArbolMB a
-- RamaB :: a -> ArbolMB a -> ArbolMB a -> ArbolMB a

-- b)
-- transformarVacio :: b
-- transformarRamaM :: a -> b -> b
-- transformarRamaB :: a -> b -> b -> b

-- c) Funcion plegarArbolMB, esta recorre el arbol dado y a medida que avanza
-- aplica las funciones correspondientes
plegarArbolMB:: b -> (a-> b -> b) -> (a -> b -> b -> b) -> ArbolMB a -> b
plegarArbolMB transVacio transRamaM transRamaB = plegar
    where
        plegar Vacio = transVacio
        plegar (RamaM x y) = transRamaM x (plegar y)
        plegar (RamaB x y z) = transRamaB x (plegar y) (plegar z)

-- d) sumarArbolMB
sumarArbolMB :: (Num a) => ArbolMB a -> a
sumarArbolMB = plegarArbolMB transVacio transRamaM transRamaB
    where
        transVacio = 0                  -- Al llegar a un arbol vacio, se debe sumar 0
        transRamaM x y = x + y          -- Al llegar a una RamaM, se suma el nodo actual con el nodo de la rama derecha
        transRamaB x y z = (x + y) + z  -- Al llegar a una RamaB, se suma el nodo actual con el nodo de la rama derecha e izquierda

-- e) aplanarArbolMB
aplanarArbolMB :: ArbolMB a -> [a]
aplanarArbolMB = plegarArbolMB transVacio transRamaM transRamaB
    where
        transVacio = []                 -- Al llegar a un arbol vacio, se agrega una lista vacia
        transRamaM x y = x:y            -- AL llegar a una RamaM, se concatena el nodo actual a la lista de nodos acumulados en la rama derecha
        transRamaB x y z = y++(x:z)     -- Al llegar a una RamaB, se concatena el nodo actual a la lista de la rama izquierda y finalmente se agrega
                                        -- a la lista de la rama derecha

-- f) analizarArbolMB
analizarArbolMB :: (Ord a) => ArbolMB a -> Maybe (a, a, Bool)
analizarArbolMB = plegarArbolMB transVacio transRamaM transRamaB
    where
        transVacio = Nothing                 -- Al llegar a un nodo vacio, se retorna Nothing
        transRamaM x y = case y of           -- Al llegar a una RamaM, se debe analizar por casos la rama derecha
                -- Si se encuentra un Maybe(a, a , Bool), acualizamos el minimo, maximo y determinamos si esta ordenada
                Just (minimo, maximo, esOrdenada) -> Just (min x minimo, max x maximo, esOrdenada && x <= maximo)
                -- Si se encuentra Nothing, quiere decir que estamos en un nodo hoja, por lo tanto de retorna 
                -- la tripleta con valores minimo y maximo el nodo actual, ademas de asumir que el arbol es ordenado
                Nothing -> Just (x, x, True)
        transRamaB x y z = case y of        -- Al llegar a una RamaM, se debe analizar por casos la rama izquierda
                -- si se encuentra un Maybe(a, a , Bool), se debe analizar por casos la rama derecha
                Just (minimo, maximo, esOrdenada) -> case z of
                                        -- Si se encuentra un Maybe(a, a , Bool), entonces actualizamos el minimo, maximo y se determina
                                        -- si es ordenada analizando en nodo padre y los nodos hijos.
                                        Just (minimo', maximo', esOrdenada') -> Just (min x $ min minimo minimo', 
                                                                                      max x $ max maximo maximo', 
                                                                                      esOrdenada && esOrdenada' 
                                                                                      && minimo <= x && x <= maximo')
                                        -- si se encuentra Nothing, actualizamos los datos a partir del analisis del nodo actual
                                        -- con la rama izquierda
                                        Nothing -> Just (min x minimo, max x maximo, esOrdenada && minimo <= x)
                -- si se encuentra Nothing, analizamos por casos la rama derecha
                Nothing -> case z of
                        -- si se encuentra un Maybe(a, a , Bool), actualizamos los datos a partir del analisis del nodo actual
                        -- con la rama derecha
                        Just (minimo', maximo', esOrdenada') -> Just (min x minimo', max x maximo', esOrdenada' && x <= maximo')
                        -- Si se encuentra Nothing, quiere decir que estamos en un nodo hoja, por lo tanto de retorna 
                        -- la tripleta con valores minimo y maximo el nodo actual, ademas de asumir que el arbol es ordenado
                        Nothing -> Just (x, x, True)
