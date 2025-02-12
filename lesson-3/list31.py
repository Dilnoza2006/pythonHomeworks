def repeat_elements(lst, times):
    return [elem for elem in lst for _ in range(times)]
print(repeat_elements([1, 2], 3))