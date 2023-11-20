-- Declaraciones del package Max_Heap

-- Librerias necesarias para la creacion del package
with Ada.Containers; use Ada.Containers;
with Ada.Containers.Vectors;
with Ada.Unchecked_Deallocation;

package Max_Heap is
    -- instanciacion de la clase vector para trabajar con enteros.
    package Integer_Vector is new 
            Ada.Containers.Vectors(Index_Type => Natural, Element_Type  => Integer);
    use Integer_Vector;
    
    -- Declaracion de tipo Nodo y Arbol
    type Nodo;
    type Arbol is access Nodo;

    -- funciones auxiliares
    function Create_Node (Elem: Integer) return Arbol;              -- crear un nodo a partir de un entero
    procedure Add_Child (Pos: Natural; Parent, Child: Arbol);       -- añadir un nodo hijo a un nodo padre.
    procedure Print_Tree (T: Arbol; Depth: Natural:= 0);            -- Impresion del arbol 
    procedure Preorder(T: Arbol; V: out Vector);                    -- Procedimiento que calcula el preorder
    procedure Postorder(T: Arbol; V: out Vector);                   -- Procedimiento que calcula el postorder
    function is_a_Max_Heap(T: Arbol) return Boolean;                -- Funcion para saber si un arbol es un Max-Heap
    function is_Symetric_Max_Heap (T: Arbol) return Boolean;        -- funcion para sabes si el arbol es un Max-Heap simetrico

    -- Definicion de tipo nodo
    type Nodo is
        record
            RamaIzq: Arbol;
            Valor_nodo: Integer;
            RamaDer: Arbol;
        end record;

    -- Procedimiento para la liberacion de memoria
    procedure Free is new Ada.Unchecked_Deallocation (Nodo, Arbol);
end Max_Heap;