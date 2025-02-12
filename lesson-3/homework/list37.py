def sum_negative(lst):
    return sum(num for num in lst if num < 0)
print(sum_negative([-3, 4, -1, 6]))