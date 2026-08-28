from DataStructures.List import array_list as lt


def new_stack():
    """Crea y retorna una pila vacia."""
    return lt.new_list()


def push(my_stack, element):
    """Agrega un elemento en el tope de la pila."""
    lt.add_last(my_stack, element)
    return my_stack


def pop(my_stack):
    """Retira y retorna el elemento del tope de la pila."""
    return lt.remove_last(my_stack)


def is_empty(my_stack):
    """Indica si la pila no contiene elementos."""
    return lt.is_empty(my_stack)


def top(my_stack):
    """Retorna el elemento del tope sin retirarlo de la pila."""
    return lt.last_element(my_stack)


def size(my_stack):
    """Retorna la cantidad de elementos de la pila."""
    return lt.size(my_stack)
