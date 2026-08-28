def new_list(): 
    newlist = {"first": None,
               "last": None,
               "size": 0,
    } 
    return newlist

def get_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count


def add_first(my_list, element):
    node = {"info": element, "next": my_list["first"]}
    my_list["first"] = node

    if my_list["size"] == 0:
        my_list["last"] = node

    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    node = {"info": element, "next": None}

    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node

    my_list["size"] += 1
    return my_list


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["first"]["info"]

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["last"]["info"]

def remove_first(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    removed = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1

    if my_list["size"] == 0:
        my_list["last"] = None
    return removed

def remove_last(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    removed = my_list["last"]["info"]

    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        node = my_list["first"]
        while node["next"] != my_list["last"]:
            node = node["next"]
        node["next"] = None
        my_list["last"] = node

    my_list["size"] -= 1
    return removed

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("list index out of range")
    if pos == 0:
        return add_first(my_list, element)
    
    if pos == my_list["size"]:
        return add_last(my_list, element)
    
    prev = my_list["first"]
    current_pos = 0
    while current_pos < pos -1:
        prev = prev["next"]
        current_pos += 1

    node = {"info": element, "next": prev["next"]}
    prev["next"] = node
    my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    if pos == 0:
        remove_first(my_list)
        return my_list
    
    prev= my_list["first"]
    current_pos = 0
    while current_pos < pos - 1:
        prev = prev["next"]
        current_pos += 1
    
    node_to_delete = prev["next"]
    prev["next"] = node_to_delete["next"]
    
    if pos == my_list["size"] - 1:
        my_list["last"] = prev
    
    my_list["size"] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    node = my_list["first"]
    current_pos = 0
    while current_pos < pos:
        node = node["next"]
        current_pos += 1
    node["info"] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        raise IndexError("list index out of range")

    if pos_1 == pos_2:
        return my_list

    node_1 = my_list["first"]
    index_1 = 0
    while index_1 < pos_1:
        node_1 = node_1["next"]
        index_1 += 1

    node_2 = my_list["first"]
    index_2 = 0
    while index_2 < pos_2:
        node_2 = node_2["next"]
        index_2 += 1

    node_1["info"], node_2["info"] = node_2["info"], node_1["info"]
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    sub = new_list()
    node = my_list["first"]
    current_pos = 0
    while current_pos < pos:
        node = node["next"]
        current_pos += 1

    copied = 0
    while node is not None and copied < num_elements:
        add_last(sub, node["info"])
        node = node["next"]
        copied += 1

    return sub