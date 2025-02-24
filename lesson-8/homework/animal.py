class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}!"

    def eat(self, food):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")

    def lay_egg(self):
        return f"{self.name} laid an egg."

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")

    def shear(self):
        return f"{self.name} is being sheared."

class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the farm.")

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, Age: {animal.age}, Sound: {animal.sound}")
            print(animal.make_sound())
            print(animal.eat("grass"))
            print(animal.sleep())
            if isinstance(animal, Cow):
                print(animal.produce_milk())
            elif isinstance(animal, Chicken):
                print(animal.lay_egg())
            elif isinstance(animal, Sheep):
                print(animal.shear())
            print()

# Example usage
if __name__ == '__main__':
    farm = Farm()
    farm.add_animal(Cow("Bessie", 5))
    farm.add_animal(Chicken("Clucky", 2))
    farm.add_animal(Sheep("Wooly", 3))
    farm.show_animals()
