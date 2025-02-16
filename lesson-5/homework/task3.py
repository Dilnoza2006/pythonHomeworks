def find_factors(n):
    """
    Find and print all factors of a positive integer n.
    
    Parameters:
        n (int): The positive integer to find factors for.
    """
    for i in range(1, n + 1):  # Iterate from 1 to n
        if n % i == 0:  # Check if i is a factor of n
            print(f"{i} is a factor of {n}")

def main():
    # Prompt the user to input a positive integer
    n = int(input("Enter a positive integer: "))
    
    # Validate the input
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        # Call the function to find and print factors
        find_factors(n)

if __name__ == "__main__":
    main()