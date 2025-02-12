def sum_positive(lst):
    return sum(num for num in lst if num > 0)
print(sum_positive([-3, 4, -1, 6]))