-- Pregunta 1, inciso (b.ii)

-- Importaciones de los paquetes Text_IO y Numerics.Real_Arrays
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Numerics.Real_Arrays; use Ada.Numerics.Real_Arrays;

-- Declaracion del procedimiento Producto_Matrices
procedure Producto_Matrices is
    -- Funcion para el llenado de una matriz cuadrada a partir del numero de filas que tendra y un string ingresado
    function Filling_Matrix_By_Space (row:Integer) return Real_Matrix is
        num_of_row:Natural:=0;                                              -- contador del numero de filas ingresadas
        Matrix: Real_Matrix(1..row,1..row):=(others => (others => 0.0));    -- Matriz de tamano row x row inicializado en 0.0
    begin
        -- En caso de que se ingrese un tamano negativo se reporta un mensaje de error
        if row < 0 then
            Put_Line("Error: la dimension de la matriz no puede ser un numero negativo");
        else 
            -- mientras que el numero de filas ingresadas sea distinto a la cantidad objetivo de estas
            while num_of_row /= row loop
                -- se le pide al usuario ingresar la fila siguiendo el formato "n1 n2 n3 ..."
                Put("Ingrese la fila nro"&Integer'Image(num_of_row+1)&" separando los numeros por espacios: ");
                declare
                    -- declaracion de variables
                    rows: String := Get_Line;   -- filas ingresadas por el usuario en formato string
                    len_of_num: Natural := 0;   -- contador para saber la longitud del numero actual, esto es, saber cuantos digitos (incluyendo el signo) tiene el numero
                    offset: Natural:= 0;        -- desplazamiento por el string
                    num_of_col: Natural:= 0;    -- contador para el numero de columnas
                begin
                    -- se recorre el string dado 
                    for J in rows'Range loop
                        -- y si en la posicion actual se encuentra un espacio
                        if rows(J..J) = " " then
                            -- se extrae del string el numero ingresado utilizando la longitud calculada del mismo y se guarda en la matriz
                            Matrix(num_of_row+1, num_of_col+1) := Float(Integer'Value(rows(offset+1..len_of_num+offset)));
                            
                            offset:= offset + len_of_num + 1;   -- se aumenta el desplazamiento necesario para continuar con la lectura de la fila
                            num_of_col := num_of_col+1;         -- se aumenta el numero de columnas
                            len_of_num := 0;                    -- y se resetea el tamano del numero actual
                        else
                            -- en caso de no encontrar un espacio en el string, se aumenta la longitud de numero
                            len_of_num := len_of_num + 1;

                            -- Si se recorrio todo el string, entonces se almacena el ultimo numero sobrante
                            if J = rows'Length then
                                Matrix(num_of_row+1, num_of_col+1) := Float(Integer'Value(rows(offset+1..len_of_num+offset)));
                            end if;                    
                        end if;
                    end loop;
                end;
                -- Se aumenta la cantidad de filas ingresadas
                num_of_row := num_of_row + 1;
            end loop;
        end if;
        -- Finalmente, se retorna la matriz
        return Matrix;
    end Filling_Matrix_By_Space;
    
    -- procedimiento para la impresion de una matriz
    procedure Show_Matrix (M: Real_Matrix) is
    begin
        for I in M'Range(1) loop
            for J in M'Range (2) loop
                Put (Integer'Image (Integer(M (I, J))) & " ");
            end loop;
            Put_Line("");
        end loop;
    end Show_Matrix;
begin
    -- se le pide al usuario ingresar las dimensiones de la matriz. Al ser cuadrada, basta con ingresar un numero
    Put("Ingrese la dimesion de la matriz cuadrada: ");

    declare
        dimesion_of_matrix:Integer := Integer'Value(Get_Line);          -- variable para almacenar el numero ingresado
        M:Real_Matrix:=Filling_Matrix_By_Space(dimesion_of_matrix);     -- matriz ingresada
    begin
        if dimesion_of_matrix < 0 then
            --finalizacion del programa por error reportado
            Put("");
        else
            -- Finalmente, se imprime el resultado
            Put_Line("El resultado es: ");

            Show_Matrix(M*Transpose(M));
        end if;
    end;
end Producto_Matrices;