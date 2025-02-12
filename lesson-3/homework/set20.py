def check_disjoint(set1, set2):
    return set1.isdisjoint(set2)

print(check_disjoint({1, 2, 3}, {4, 5, 6}))  
print(check_disjoint({1, 2, 3}, {3, 4, 5}))