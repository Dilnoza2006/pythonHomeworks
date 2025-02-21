from math import sqrt

class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("A vector must have at least one component.")
        self.components = components

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __eq__(self, other):
        return self.components == other.components

    def _validate_dimensions(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions.")

    def __add__(self, other):
        self._validate_dimensions(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        self._validate_dimensions(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(*(a * scalar for a in self.components))
        raise ValueError("Multiplication is only supported with a scalar.")

    def __rmul__(self, scalar):
        return self * scalar

    def dot(self, other):
        self._validate_dimensions(other)
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        return sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(3 * v1)
print(v1.dot(v2))
print(v1.magnitude())
print(v1.normalize())
