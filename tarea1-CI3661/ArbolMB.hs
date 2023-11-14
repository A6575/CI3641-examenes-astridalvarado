module ArbolMB where
import Data.Maybe 

data ArbolMB a = Vacio
                | RamaM a (ArbolMB a)
                | RamaB a (ArbolMB a) (ArbolMB a)
                deriving Show

-- Vacio :: ArbolMB a
-- RamaM :: a -> ArbolMB a -> ArbolMB a
-- RamaB :: a -> ArbolMB a -> ArbolMB a -> ArbolMB a

-- transformarVacio :: b
-- transformarRamaM :: a -> b -> b
-- transformarRamaB :: a -> b -> b -> b

plegarArbolMB:: b -> (a-> b -> b) -> (a -> b -> b -> b) -> ArbolMB a -> b
plegarArbolMB transVacio transRamaM transRamaB = plegar
    where
        plegar Vacio = transVacio
        plegar (RamaM x y) = transRamaM x (plegar y)
        plegar (RamaB x y z) = transRamaB x (plegar y) (plegar z)

sumarArbolMB :: (Num a) => ArbolMB a -> a
sumarArbolMB = plegarArbolMB transVacio transRamaM transRamaB
    where
        transVacio = 0
        transRamaM x y = x + y
        transRamaB x y z = (x + y) + z

aplanarArbolMB :: ArbolMB a -> [a]
aplanarArbolMB = plegarArbolMB transVacio transRamaM transRamaB
    where
        transVacio = []
        transRamaM x y = x:y
        transRamaB x y z = y++(x:z)

analizarArbolMB :: (Ord a) => ArbolMB a -> Maybe (a, a, Bool)
analizarArbolMB = plegarArbolMB transVacio transRamaM transRamaB
    where
        transVacio = Nothing
        transRamaM x y = case y of
                Just (minimo, maximo, esOrdenada) -> Just (min x minimo, max x maximo, esOrdenada && x <= maximo)
                Nothing -> Just (x, x, True)
        transRamaB x y z = case y of
                Just (minimo, maximo, esOrdenada) -> case z of
                                        Just (minimo', maximo', esOrdenada') -> Just (min x $ min minimo minimo', 
                                                                                      max x $ max maximo maximo', 
                                                                                      esOrdenada && esOrdenada' 
                                                                                      && minimo <= x && x <= maximo')
                                        Nothing -> Just (min x minimo, max x maximo, esOrdenada && minimo <= x)
                Nothing -> case z of
                        Just (minimo', maximo', esOrdenada') -> Just (min x minimo', max x maximo', esOrdenada' && x <= maximo')
                        Nothing -> Just (x, x, True)
