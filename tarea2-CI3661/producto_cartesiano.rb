# función que implementa el iterador que obtiene el producto cartensiano de dos listas.
def producto_cartesiano(lista1, lista2)
    # se verifica que ambos argumentos sean de tipo Array
    if lista1.class != Array or lista2.class != Array
        raise "Ambos elementos deben ser de tipo Array"
    end

    # Se itera por la primera lista
    for item1 in lista1
        # Se itera por la segunda lista
        for item2 in lista2
            # y se realiza yield de la sublista con los elementos de la primera
            # y segunda lista, realizando el producto cartesiado entre estas
            yield ([item1,item2])
        end
    end
end

# función auxiliar para poder observar el comportamiento del iterador creado
def iterador(lista1,lista2)
    # se llama a la función producto_cartesiado con la función lambda necesaria
    # para poder imprimir el pantalla los valores generados
    producto_cartesiano(lista1, lista2) {|x| puts "#{x}"}
end
