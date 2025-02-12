def remove_element(s, element):
    s.discard(element)  # Avoids KeyError if element is absent
    return s

print(remove_element({1, 2, 3}, 2)) 