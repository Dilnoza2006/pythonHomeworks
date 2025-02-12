import random

def generate_random_set(size, start, end):
    return set(random.sample(range(start, end + 1), size))

print(generate_random_set(5, 1, 20))