def index_of_element(lst, element):
    return lst.index(element) if element in lst else -1 
print(index_of_element([5, 8, 2, 8], 8)) 
print(index_of_element([1, 2, 3], 4))  