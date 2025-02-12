def repeat_elements(tpl, times):
    return tuple(x for x in tpl for _ in range(times))

print(repeat_elements((1, 2, 3), 2)) 