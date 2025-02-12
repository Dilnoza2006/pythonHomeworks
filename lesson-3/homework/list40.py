def get_unique_ordered(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
print(get_unique_ordered([4, 1, 2, 4, 3, 2, 1])) 