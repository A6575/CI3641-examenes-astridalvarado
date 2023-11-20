with Ada.Text_IO;
with Max_Heap; use Max_Heap;

procedure Main is
    Root : Arbol;
begin
   -- Crear un árbol de enteros
   Root := Create_Node(5);
   Add_Child(0, Root, Create_Node(5));
   Add_Child(1, Root, Create_Node(5));
   Add_Child(0, Root.RamaIzq, Create_Node(5));
   Add_Child(1, Root.RamaIzq, Create_Node(5));
   
   -- Imprimir el árbol de enteros
   Print_Tree(Root);
   
   -- Si el arbol es un Max_Heap simetrico, entonces se le indica a usuario
   if is_Symetric_Max_Heap(Root) then
        Ada.Text_IO.Put_Line("El arbol es un max-heap simetrico");
   else
        Ada.Text_IO.Put_Line("El arbol no es un max-heap simetrico");
   end if;
end Main;