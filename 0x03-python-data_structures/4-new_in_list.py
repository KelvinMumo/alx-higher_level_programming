#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        pass
    elif idx >= 0 and idx < len(my_list):
        i = my_list[:]
        i[idx] = element
        return i
    else:
        return my_list
