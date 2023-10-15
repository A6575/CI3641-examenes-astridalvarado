-- Pregunta 1, inciso (b.i)

-- Importaciones de los paquetes Text_IO, Strings y Strings.Unbounded
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings; use Ada.Strings;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

-- Declacion del procedimiento Rotar_String
procedure Rotar_String is
    -- Declaraciones de variables usadas en el procedimiento:
    mod_num_len: Integer:= 0;                                   -- Variable para almacenar el valor resultante de 'num_of_rotation mod len_of_string' 
begin
    Put("Ingrese la palabra que desee rotar: ");
    declare
        string_to_rotate: String := Get_Line;                       -- String ingresado por el usuario
        len_of_string: Natural := string_to_rotate'Length;          -- longitud del string ingresado
        rotated_string:String(1..len_of_string);                   -- Variable para almacenar el string una vez haya sido rotado
    begin
        Put("Ingrese la cantidad de caracteres a rotar de su palabra: ");
        declare
            num_for_rotation: Integer := Integer'Value(Get_Line);       -- Numero ingresado por el usuario
        begin
             -- Se verifica que el numero para realizar la rotacion sea un numero no-negativo
            if num_for_rotation<0 then
                Put_Line("El numero ingresado debe ser mayor o igual a 0");
            else
                -- En caso de que el usuario ingrese la cadena vacia "", se retorna la misma
                if string_to_rotate'Length = 0 then
                    Put_Line(string_to_rotate);
                else
                    -- se calcula el modulo del numero ingresado para las rotaciones 
                    -- con respecto a la longitud del string ingresado para saber el 
                    -- tamano se las subcadenas para realizar la rotacion
                    mod_num_len := num_for_rotation mod len_of_string;

                    -- en caso de que este valor sea 0, es decir, es multiplo de la longitud del string
                    -- entonces se imprime la caneda original
                    if (mod_num_len = 0) then
                        Put_Line(string_to_rotate);
                    else
                        -- se selecciona las primeros mod_num_len caracteres del string ingresado y se
                        -- almacenan en los ultimos mod_num_len caracteres de rotated_string. De esta forma
                        -- se hacer la rotacion correspondiente
                        rotated_string (len_of_string-(mod_num_len-1)..len_of_string):= string_to_rotate(1..mod_num_len);
                        
                        -- Luego, se selecciona el resto del string ingresado y se posiciona al principio del
                        -- string resultado
                        rotated_string (1.. len_of_string-mod_num_len) := string_to_rotate(mod_num_len+1..len_of_string);

                        -- finalmente, se imprime el string resultante
                        Put_Line(rotated_string);
                    end if;
                end if;
            end if;
        end;
    end; 
end Rotar_String;