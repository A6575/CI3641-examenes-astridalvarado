with Ada.Text_IO;
with Ada.Unchecked_Deallocation;

procedure Main is
    -- declaracion de tipo Church como tipo etiquetado
    type Church is tagged;
    -- declaracion de tipo Church_Suc como apuntador al tipo Church
    type Church_Suc is access Church;
    
    -- se crea el cuerpo del tipo Church como un record con atributo igual a Church_Suc
    type Church is tagged 
        record
            Succesor: Church_Suc;
        end record;
    
    -- Constructor Zero
    function Zero return Church_Suc is
    begin
        return null;
    end Zero;

    -- Constructor Suc()
    function Suc(N : Church_Suc) return Church_Suc is
        S: Church_Suc;
    begin
        S := new Church'(Succesor => N); 
        return S;
    end Suc;

    -- Procedimiento Free para liberacion de memoria
    procedure Free is new Ada.Unchecked_Deallocation (Church, Church_Suc);
    
    -- Procedimiento para la impresion en consola del tipo Church
    procedure Print_Church(N : Church_Suc) is
    begin
        if N.all.Succesor = null then
            Ada.Text_IO.Put("Suc(Zero)");
        else
            Ada.Text_IO.Put("Suc(");
            Print_Church(N.all.Succesor);
            Ada.Text_IO.Put(")");
        end if;
    end Print_Church;

    -- Funcion que, dado un numero natural, representa dicho numero como el tipo Church 
    function Create_Suc(N: Natural) return Church_Suc is
    begin
        if N = 0 then
            return Zero;
        else
            return Suc(Create_Suc(N-1));
        end if;
    end Create_Suc;

    -- Funcion que, dado dos numeros naturales, realiza la suma de dichos numeros y retorna
    -- la representacion de su resultado como un tipo Church
    function Suma(N,M: Natural) return Church_Suc is
    begin
        return Create_Suc(N+M);
    end Suma;

    -- Funcion que, dado dos numeros naturales, realiza la multiplicacion de dichos numeros 
    -- y retorna la representacion de su resultado como un tipo Church
    function Multiplicacion(N,M:Natural) return Church_Suc is
    begin
        return Create_Suc(N*M);
    end;
    
    -- Variables del programa principal.
    N : Church_Suc := Suma(4,6);
    M : Church_Suc := Multiplicacion(2,3);
begin
    Print_Church(N);                -- Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Suc(Zero))))))))))
    Free(N);
    Ada.Text_IO.Put_Line("");       
    Print_Church(M);                -- Suc(Suc(Suc(Suc(Suc(Suc(Zero))))))
    Free(M);
end Main;