% Pregunta 2 - arbol
% arbol de prueba
/*
         a
        / \
       c   b
      / \   \
     i  g    d
         \    \
          h    e
                \
                 f
                / \
               j   k   
*/
arco(a,b).
arco(a,c).
arco(b,d).
arco(c,g).
arco(d,e).
arco(e,f).
arco(g,h).
arco(c,i).
arco(f,j).
arco(f,k).

/*a) predicado 'hermano'*/
hermano(Nodo1, Nodo2) :- arco(Padre, Nodo1), arco(Padre, Nodo2).

/*b) predicado 'alcanzable'*/
% dfs/3 para buscar un camino desde A hasta B
dfs(A, B, Camino) :-
    dfs(A, B, [A], Camino).

% dfs/4 auxiliar que lleva la pila de visitados   
dfs(A, B, Visitados, Camino) :-  A = B, Camino = Visitados.
dfs(A, B, Visitados, Camino) :-
    arco(A,X),
    not(member(X, Visitados)),
    dfs(X, B, [X|Visitados], Camino).

% predicado alcanzable para verificar si dos nodos son alcanzables
alcanzable(X, Y) :- 
    dfs(X,Y, L),
    member(Y, L).

/*c) predicado 'lca'*/
% predicado lca para encontrar el nodo lca de dos nodos
lca(Nodo1, Nodo2, Nodo3) :- 
    alcanzable(Nodo3, Nodo1), 
    alcanzable(Nodo3, Nodo2), 
    not((alcanzable(Nodo3, Nodo_k),
         Nodo_k \= Nodo3,
         alcanzable(Nodo_k, Nodo1),
         alcanzable(Nodo_k, Nodo2))).

/*d) predicado 'tree'*/
% predicado tree para verificar si todos los nodos alcanzables desde un nodo A forman un arbol
% se debe verificar que existan N nodos y N-1 aristas
tree(Raiz) :-
    nodos_aristas(Raiz, Cantidad_nodos, Cantidad_aristas),
    Cantidad_nodos is Cantidad_aristas + 1.

% nodos_aristas cuenta nodos y aristas    
nodos_aristas(Raiz, N, A) :-
    setof(Nodo, alcanzable(Raiz, Nodo), Nodos),
    length(Nodos, N),
    findall(Arista, arco(Arista, _), Aristas), 
    length(Aristas, A).