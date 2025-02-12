def remove_element(tpl, element):
    lst = list(tpl)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

print(remove_element((1, 2, 3, 2, 4), 2))