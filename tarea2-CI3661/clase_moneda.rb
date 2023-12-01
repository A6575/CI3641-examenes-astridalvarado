# Clase Moneda
class Moneda
    # se utilizar attr_accessor para que cantidad
    # funcione como setter y getter
    attr_accessor :cantidad
    
    # Inicializador de la clase
    def initialize(cantidad)
        # si la cantidad es negativa, se levanta un error
        if cantidad < 0
            raise "Cantidad ingresada invalida"
        end

        @cantidad = cantidad
    end

    # definición del método en para la conversión de monedas
    def en(atomo)
        # se inicializa una lista vacía. Se tiene la siguiente convencion
        #   - 1ra posicion: conversion correspondiente a Dolar
        #   - 2da posicion: conversion correspondiente a Yen
        #   - 3ra posicion: conversion correspondiente a Euro
        #   - 4ta posicion: conversion correspondiente a Bolivar
        #   - 5ta posicion: conversion correspondiente a Bitcoin
        conversion = []

        # el cual se inicializa dependiendo de la clase actual
        case
            when self.class == Dolar
                conversion = [1,147.17,0.9113,35.50,0.000027]
            when self.class == Yen
                conversion = [(1/147.17),1,0.0062,0.24,0.0000001796]
            when self.class == Euro
                conversion = [(1/0.9113),(1/0.0062),1,38.93,0.00002909]
            when self.class == Bolivar
                conversion = [(1/35.50),(1/0.24),(1/38.93),1,0.00000074699]
            when self.class == Bitcoin
                conversion = [(1/0.000027),(1/0.0000001796),(1/0.00002909),(1/0.00000074699),1]
            when self.class == Moneda
                # si la clase es Moneda, no se realiza conversión alguna
                conversion = [1,1,1,1,1]
            else
                raise "Subclase no definida"
        end

        # Se realiza un analisis por casos del átomo pasado como argumento, para así poder
        # hacer la conversión correspondiente
        case atomo
            when :dolares
                Dolar.new(conversion[0]*@cantidad)
            when :yenes
                Yen.new(conversion[1]*@cantidad)
            when :euros
                Euro.new(conversion[2]*@cantidad)
            when :bolivares
                Bolivar.new(conversion[3]*@cantidad)
            when :bitcoins
                Bitcoin.new(conversion[4]*@cantidad)
            else
                raise "Cambio invalido"
        end
    end

    # Metodo comparar para realizar la comparación entre modenas.
    def comparar(moneda)
        # se inicializa una variable con valor inicial -2
        comparacion = -2
        # se analiza por casos, dependiendo del tipo de Moneda encontrada.
        # Se utiliza el método en para evitar preguntar por el tipo de ambas monedas.
        # Se hace uso de la función <=> con el fin de realizar una única comparación
        case
            when self.class == Moneda
                raise "Es necesario especificar la subclase de Moneda a la que se desea realizar la comparación" 
            when self.en(:dolares).cantidad == self.cantidad
                comparacion = @cantidad <=> moneda.en(:dolares).cantidad 
            when self.en(:yenes).cantidad == self.cantidad
                comparacion = @cantidad <=> moneda.en(:yenes).cantidad 
            when self.en(:euros).cantidad == self.cantidad
                comparacion = @cantidad <=> moneda.en(:euros).cantidad 
            when self.en(:bolivares).cantidad == self.cantidad
                comparacion = @cantidad <=> moneda.en(:bolivares).cantidad 
            when self.en(:bitcoins).cantidad == self.cantidad
                comparacion = @cantidad <=> moneda.en(:bitcoins).cantidad 
            else
                raise "Subclase no definida"
        end

        # Se analiza por casos el valor obtenido
        case comparacion
            when -1
                :menor
            when 0
                :igual
            when 1
                :mayor
            else
                raise "Error al comparar las monedas"
        end
    end
end

### Subclases de Moneda

# Subclase Dolar
class Dolar < Moneda 
end

# Subclase Yen
class Yen < Moneda 
end

# Subclase Euro
class Euro < Moneda 
end

# Subclase Bolivar
class Bolivar < Moneda 
end

# Subclase Bitcoin
class Bitcoin < Moneda
end

# Ampliación de la clase Float para agregar los métodos de conversión a monedas
class Float
  def dolares
    Dolar.new(self)
  end

  def yenes
    Yen.new(self)
  end

  def euros
    Euro.new(self)
  end

  def bolivares
    Bolivar.new(self)
  end

  def bitcoins
    Bitcoin.new(self)
  end
end