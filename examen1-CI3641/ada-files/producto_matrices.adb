-- Pregunta 1, inciso (b.ii)

with Ada.Text_IO; use Ada.Text_IO;
with Ada.Numerics.Real_Arrays; use Ada.Numerics.Real_Arrays;
procedure Producto_Matrices is
    function Filling_Matrix_By_Space (row:Integer) return Real_Matrix is
        num_of_row:Natural:=0;
        Matrix: Real_Matrix(1..row,1..row):=(others => (others => 0.0));
    begin
        while num_of_row /= row loop
            Put("Ingrese la fila nro"&Integer'Image(num_of_row+1)&" separando los numeros por espacios: ");
            declare
                rows: String := Get_Line;
                len_of_num: Natural := 0;
                offset: Natural:= 0;
                num_of_col: Natural:= 0;
            begin
                for J in rows'Range loop
                    if rows(J..J) = " " then
                        if num_of_col > row then
                            Put_Line("El numero de columnas debe coincidir con el numero de filas.");
                        end if;
                        Matrix(num_of_row+1, num_of_col+1) := Float(Integer'Value(rows(offset+1..len_of_num+offset)));
                        offset:= offset + len_of_num + 1;
                        num_of_col := num_of_col+1;
                        len_of_num := 0;
                    else
                        len_of_num := len_of_num + 1;
                        if J = rows'Length then
                            Matrix(num_of_row+1, num_of_col+1) := Float(Integer'Value(rows(offset+1..len_of_num+offset)));
                        end if;                    
                    end if;
                end loop;
            end;
            num_of_row := num_of_row + 1;
        end loop;
        return Matrix;
    end Filling_Matrix_By_Space;

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
    Put("Ingrese la dimesion de la matriz cuadrada: ");

    declare
        dimesion_of_matrix:Integer := Integer'Value(Get_Line);
        M:Real_Matrix:=Filling_Matrix_By_Space(dimesion_of_matrix);
    begin
        Put_Line("El resultado es: ");

        Show_Matrix(M*Transpose(M));
    end;
end Producto_Matrices;