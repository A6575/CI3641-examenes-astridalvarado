-- Implementacion del cuerpo del package Max_Heap

with Ada.Text_IO;
with Ada.Strings; use Ada.Strings;
with Ada.Containers; use Ada.Containers;
with Ada.Containers.Vectors;

package body Max_Heap is
    
    -- Funcion que dado un entero, se retorna un arbol con el valor ingresado como nodo principal
    function Create_Node(Elem: Integer) return Arbol is
        N: Arbol := new Nodo;
    begin
        N.Valor_nodo := Elem;
        return N;
    end Create_Node;

    -- Funcion que dada una posicion, un Arbol padre y un arbol hijo, se añade al arbol padre
    -- el nuevo arbol hijo en dicha posicion. Se tiene que si Pos es 0, entonces se agrega una
    -- Rama izquierda, para el caso contrario, una Rama dereha
    procedure Add_Child (Pos: Natural; Parent, Child: Arbol) is
    begin
        if Pos = 0 then
            Parent.RamaIzq := Child;
        else
            Parent.RamaDer := Child;
        end if;
    end Add_Child;

    -- Funcion que imprime cierto arbol dado de forma vertical
    procedure Print_Tree (T: Arbol; Depth: Natural := 0) is
    begin
        if T /= null then
        
            Print_Tree(T.RamaDer, Depth + 1);
            for I in 1 .. Depth loop
                Ada.Text_IO.Put("    ");
            end loop;
            Ada.Text_IO.Put_Line(T.Valor_Nodo'Image);
            Print_Tree(T.RamaIzq, Depth + 1);

        end if;
    end Print_Tree;

    -- Procedimiento para obtener un vector con los nodos del arbol en orden Preorder
    procedure Preorder (T: Arbol; V: out Vector) is
    begin
        if T /= null then
            V.Append(T.Valor_nodo);
            Preorder (T.RamaIzq, V);
            Preorder (T.RamaDer, V);
        end if;
    end Preorder;

    -- Procedimiento para obtener un vector con los nodos del arbol en orden Postorder
    procedure Postorder (T: Arbol; V: out Vector) is
    begin
        if T /= null then
            Postorder (T.RamaIzq, V);
            Postorder (T.RamaDer, v);
            V.Append(T.Valor_nodo);
        end if;
    end Postorder;

    -- Funcion que, dado un arbol, indica si un arbol es un Max_Heap recorriendo todo el arbol y verificando que
    -- tanto la rama izquierda como la rama derecha cumplan con que el valor del nodo padre es mayor o igual a 
    -- el valor de los nodos a la izquierda y derecha
    function is_a_Max_Heap(T: Arbol) return Boolean is
        VRamaIzq : Boolean:= False;
        VRamaDer : Boolean:= False;
    begin
        if T /= null then
            if T.RamaIzq /= null then
                if T.Valor_nodo >= T.RamaIzq.Valor_nodo then
                    VRamaIzq:=True;
                end if;
            else
                VRamaIzq := True;
            end if;

            if T.RamaDer /= null then
                if T.Valor_nodo >= T.RamaDer.Valor_nodo then
                    VRamaDer:=True;
                end if;
            else
                VRamaDer := True;
            end if;

            return VRamaDer and VRamaIzq and is_a_Max_Heap(T.RamaIzq) and is_a_Max_Heap(T.RamaDer);
        end if;

        return True;
    end is_a_Max_Heap;

    -- Funcion que verifica que un arbol sea un Max_Heap y ademas que el recorrido Postorder y 
    -- Preorder son iguales
    function is_Symetric_Max_Heap (T: Arbol) return Boolean is
        Vector_Preorder: Vector;
        Vector_Postorder: Vector;
        is_Max_Heap: Boolean;
        is_Symetric: Boolean := True;
        aux: Extended_Index;
        aux1: Extended_Index;
    begin
        Preorder(T, Vector_Preorder);
        Postorder(T, Vector_Postorder);
        is_Max_Heap := is_a_Max_Heap(T);

        if is_Max_Heap then
            for VP of Vector_Preorder loop
                aux := Vector_Postorder.Find_Index(VP);
                aux1 := Vector_Preorder.Find_Index(VP);
                if aux /= aux1 then
                    is_Symetric := False;
                    exit;
                end if;
            end loop;
        end if;

        return is_Max_Heap and is_Symetric;
    end is_Symetric_Max_Heap;

end Max_Heap;