from buddy_system import *

def test_Buddy_System ():
    bs = Buddy_System(14)
    assert( bs.block_list == [[14,""]] and bs.power_of_two == 3 and bs.list_of_free_block == [[1,0],[2,0],[4,0],[8,0]])

def test_Buddy_System_reserva ():
    bs = Buddy_System(14)
    bs.reservar(5, "nombre1")
    bs.reservar(6, "nombre2")
    bs.reservar(2, "nombre3")
    assert (bs.block_list == [[5, "nombre1"], [6, "nombre2"], [2,"nombre3"], [1, ""]])

def test_Buddy_System_liberar ():
    bs = Buddy_System(14)
    
    bs.reservar(5, "nombre1")
    bs.reservar(6, "nombre2")
    bs.reservar(2, "nombre3")

    bs.liberar("nombre2")
    assert (bs.block_list == [[5, "nombre1"], [6, ""], [2,"nombre3"], [1, ""]])
    bs.liberar("nombre3")
    assert (bs.block_list == [[5, "nombre1"], [9, ""]])
    bs.liberar("nombre1")
    assert (bs.block_list == [[14, ""]])

def test_Buddy_System_mostrar ():
    bs = Buddy_System(14)
    bs.mostrar()
    assert(bs.list_of_free_block == [[1,0],[2,1],[4,1],[8,1]])
    bs.reservar(5, "nombre1")
    bs.mostrar()
    assert(bs.list_of_free_block == [[1,1],[2,0],[4,0],[8,1]])
