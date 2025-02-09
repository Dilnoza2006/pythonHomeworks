import itertools

txt = "LMaasleitbtui"
car_brands = {"Tesla", "BMW", "Audi", "Ford", "Buick", "Toyota", "Mazda"}

possible_substrings = set(
    "".join(p) for i in range(1, len(txt) + 1) for p in itertools.permutations(txt, i)
)

found_cars = car_brands.intersection(possible_substrings)
print("Extracted Car Names:", found_cars)
