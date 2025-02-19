def check(func):
    def wrapper(numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        return func(numerator, denominator)
    return wrapper

@check
def divide(numerator, denominator):
    return numerator / denominator

# Example usage:
try:
    result = divide(10, 2)
    print("Result:", result)
except ValueError as e:
    print(e)

try:
    result = divide(10, 0)
    print("Result:", result)
except ValueError as e:
    print(e)