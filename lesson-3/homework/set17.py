def filter_odd_numbers(s):
    return {x for x in s if x % 2 != 0}

print(filter_odd_numbers({1, 2, 3, 4, 5, 6})) 