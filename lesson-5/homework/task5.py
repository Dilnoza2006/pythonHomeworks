def is_prime(n):
    """
    Check if a positive integer n is a prime number.
    
    Parameters:
        n (int): The number to check.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Other even numbers are not prime
    
    # Check for factors from 3 to the square root of n, skipping even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False  # If n is divisible by any number, it's not prime
    return True  # If no factors are found, n is prime
# Test the function
print(is_prime(2))    # Output: True
print(is_prime(3))    # Output: True
print(is_prime(4))    # Output: False
print(is_prime(29))   # Output: True
print(is_prime(30))   # Output: False
print(is_prime(1))    # Output: False
print(is_prime(-5))   # Output: False