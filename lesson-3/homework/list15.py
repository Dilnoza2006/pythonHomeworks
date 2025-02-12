def count_even(lst):
    return sum(1 for num in lst if num % 2 == 0)
print(count_even([1, 2, 3, 4, 5, 6]))