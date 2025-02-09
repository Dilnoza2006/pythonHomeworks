string = input("Enter a string: ")
vowels = "AEIOUaeiou"
symbol = "*"
new_string = "".join(symbol if char in vowels else char for char in string)
print(new_string)
