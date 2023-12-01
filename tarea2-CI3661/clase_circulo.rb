# Clase Circulo
class Circulo

    # Implementacion de getter
    def radio
        @radio
    end

    # Implementacion de setter
    def radio=(radio)
        @radio = radio
    end
    
    # Implementacion de inicializador
    def initialize(radio)
        # si el radio es negativo, se levanta una excepción
        if radio < 0
            raise "Radio Invalido"
        end
        @radio = radio
    end

    # Metodo para obtener el area de un circulo
    # redondeado a 4 decimales.
    def area
        (Math::PI*(@radio**2)).floor(4)
    end
end

# Clase Cilindro
class Cilindro < Circulo

    # Implementacion de getter para radio
    def radio
        @radio
    end

    # Implementacion de setter para radio
    def radio=(radio)
        @radio = radio
    end

    # Implementacion de getter para altura
    def altura
        @altura
    end

    # Implementacion de setter para altura
    def altura=(altura)
        @altura = altura
    end

    # Implementacion de inicializador
    def initialize(radio, altura)
         # si el radio es negativo, se levanta una excepción
        if radio < 0
            raise "Radio Invalido"
        end

         # si la altura es negativa, se levanta una excepción
        if altura < 0
            raise "Altura Invalida"
        end

        @altura = altura
        @radio = radio
    end

    # Metodo para obtener el volumen de un cilindro
    # redondeado a 4 decimales. Se utiliza la función
    # de area propia de Circulo.
    def volumen
        (area*@altura).floor(4)
    end
end
