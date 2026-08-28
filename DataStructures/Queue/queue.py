from DataStructures.List import single_linked_list as lt


def new_queue():
	"""Crea y retorna una cola vacia."""
	return lt.new_list()


def enqueue(my_queue, element):
	"""Agrega un elemento al final de la cola."""
	lt.add_last(my_queue, element)
	return my_queue


def dequeue(my_queue):
	"""Retira y retorna el primer elemento de la cola."""
	if lt.is_empty(my_queue):
		raise Exception("EmptyStructureError: queue is empty")
	return lt.remove_first(my_queue)


def is_empty(my_queue):
	"""Indica si la cola no contiene elementos."""
	return lt.is_empty(my_queue)


def peek(my_queue):
	"""Retorna el primer elemento sin retirarlo de la cola."""
	if lt.is_empty(my_queue):
		raise Exception("EmptyStructureError: queue is empty")
	return lt.first_element(my_queue)


def size(my_queue):
	"""Retorna la cantidad de elementos de la cola."""
	return lt.size(my_queue)
