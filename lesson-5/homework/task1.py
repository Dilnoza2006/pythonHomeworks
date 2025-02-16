def convert_cel_to_far(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def convert_far_to_cel(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    # Prompt user for a temperature in Fahrenheit and convert to Celsius
    fahrenheit = float(input("Enter a temperature in degrees Fahrenheit: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit}°F is equivalent to {round(celsius, 2)}°C.\n")

    # Prompt user for a temperature in Celsius and convert to Fahrenheit
    celsius = float(input("Enter a temperature in degrees Celsius: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius}°C is equivalent to {round(fahrenheit, 2)}°F.")

if __name__ == "__main__":
    main()