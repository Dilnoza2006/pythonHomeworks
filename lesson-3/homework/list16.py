def count_odd(lst):
    return sum(1 for num in lst if num % 2 == 1)
print(count_odd([1, 2, 3, 4, 5, 6]))