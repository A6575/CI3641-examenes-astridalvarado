-- Pregunta 1, inciso (b.i)

-- Importaciones de los paquetes Text_IO, Strings y Strings.Unbounded
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings; use Ada.Strings;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;

-- Declacion del procedimiento Rotar_String
procedure Rotar_String is
    -- Declaraciones de variables usadas en el procedimiento:
    string_to_rotate: String := Get_Line;                       -- String ingresado por el usuario
    num_for_rotation: Integer := Integer'Value(Get_Line);       -- Numero ingresado por el usuario
    len_of_string: Natural := string_to_rotate'Length;          -- longitud del string ingresado
    mod_num_len: Integer:= 0;                                   -- Variable para almacenar el valor resultante de 'num_of_rotation mod len_of_string' 
    split_string: Unbounded_String := To_Unbounded_String("");  -- Variable del tipo string con longitud variable para almacenar las diferentes separaciones del string ingresado
    string_reversed:String(1..len_of_string);                   -- Variable para almacenar el string una vez haya sido rotado
    can_be_splited:Boolean:=True;                               -- Variable para indicar la posibilidad de realizar una rotacion
    offset: Natural := 0;                                       -- Variable para llenar registro del esplazamiento requerido 
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
                -- Mientras se pueda separar el string ingresado
                while can_be_splited loop
                    -- se calcula el string a partir del desplazamiento a realizar
                    split_string := To_Unbounded_String(string_to_rotate(offset+1..len_of_string));
                    
                    -- y si este string tiene una longitud mayor estricta al modulo
                    if To_String(split_string)'Length > mod_num_len then
                        -- entonces al string original se le selecciona la subcadena de tamano mod_num_len
                        -- y es almacenado al final de la subcadena de variable de resultado. Observe el siguiente ejemplo
                        -- para el input "hola" con 2 rotaciones:
                        -- 
                        -- string_to_rotate(0+1..2+0) = string_to_rotate(1..2) = "ho"
                        -- string_reversed(4-0-(2-1)..4-0) = string_reversed(3..4) = "ho"
                        --
                        -- Por lo tanto string_reversed tiene en sus dos ultimas posiciones la subcadena "ho" 
                        string_reversed (len_of_string-offset-(mod_num_len-1)..len_of_string-offset):= string_to_rotate(offset+1..mod_num_len+offset);

                        -- se incrementa el desplazamiento 
                        offset := offset + mod_num_len;
                    else
                        -- En caso de que el tamano de split_string sea igual o menor al modulo, basta con colocar la candena
                        -- restante al principio del string de resultado y se indica que ya no es posible seguir rotando el string
                        string_reversed (1..To_String(split_string)'Length) := string_to_rotate(offset+1..len_of_string);
                        can_be_splited := False;
                    end if;
                end loop;
                -- finalmente, se imprime el string resultante
                Put_Line(string_reversed);
            end if;
        end if;
    end if;
end Rotar_String;