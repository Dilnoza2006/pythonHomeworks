def invest(amount, rate, years):
    """
    Calculate and print the growth of an investment over a specified number of years.
    
    Parameters:
        amount (float): The initial principal amount.
        rate (float): The annual rate of return (as a decimal).
        years (int): The number of years to calculate the investment growth.
    """
    for year in range(1, years + 1):
        amount *= (1 + rate)  # Increase the amount by the annual rate of return
        print(f"year {year}: ${round(amount, 2)}")

def main():
    # Prompt the user for input
    amount = float(input("Enter the initial principal amount: "))
    rate = float(input("Enter the annual rate of return (as a decimal): "))
    years = int(input("Enter the number of years to calculate: "))

    # Call the invest function with the user's inputs
    invest(amount, rate, years)

if __name__ == "__main__":
    main()