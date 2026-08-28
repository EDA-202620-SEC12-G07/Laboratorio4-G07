from DataStructures.List import single_linked_list as lt


def new_stack():
    """Crea y retorna una pila vacia."""
    return lt.new_list()


def push(my_stack, element):
    """Agrega un elemento en el tope de la pila."""
    lt.add_first(my_stack, element)
    return my_stack


def pop(my_stack):
    """Retira y retorna el elemento del tope de la pila."""
    if lt.is_empty(my_stack):
        raise Exception("EmptyStructureError: stack is empty")
    element = lt.get_element(my_stack, 0)
    lt.remove_first(my_stack)
    return element


def is_empty(my_stack):
    """Indica si la pila no contiene elementos."""
    return lt.is_empty(my_stack)


def top(my_stack):
    """Retorna el elemento del tope sin retirarlo de la pila."""
    if lt.is_empty(my_stack):
        raise Exception("EmptyStructureError: stack is empty")
    return lt.first_element(my_stack)


def size(my_stack):
    """Retorna la cantidad de elementos de la pila."""
    return lt.size(my_stack)
