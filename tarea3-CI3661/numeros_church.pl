% Pregunta 1 - numeros de Church

% a) Suma

suma(X, *, X) :- !.
suma(X, up(Y), up(Z)) :- suma(X, Y, Z).

% b) Resta  

resta(X, *, X) :- !. 
resta(up(X), up(Y), Z) :- resta(X, Y, Z).

% c) Multiplicacion

mult(_, *, *) :- !.
mult(X, up(Y), Z) :- mult(X, Y, W), suma(W, X, Z).

