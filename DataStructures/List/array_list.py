# Implementación de funciones
# Implementación de una lista dinámica utilizando un arreglo (array list)
def new_list():
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist

# Implementación de funciones para la lista dinámica
def get_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    return my_list["elements"][pos]


def is_present(my_list, element, cmp_function):
    for position in range(my_list["size"]):
        info = my_list["elements"][position]

        if cmp_function(element, info) == 0:
            return position

    return -1


def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][0]

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][my_list["size"] -1]

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] ==0:
        raise IndexError("list index out of range")
    removed = my_list["elements"].pop(0)
    my_list["size"] -= 1
    return removed

def remove_last(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    removed = my_list["elements"].pop(my_list["size"]-1)
    my_list["size"] -= 1
    return removed

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"][pos_1], my_list["elements"][pos_2] = my_list["elements"][pos_2], my_list["elements"][pos_1]
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"]: 
        raise IndexError("list index out of range")
    sub = new_list()
    end = pos_i + num_elements
    for i in range(pos_i, end):
        if i >= my_list["size"]:
            break
        sub["elements"].append(my_list["elements"][i])
        sub["size"] += 1
    return sub


            

    