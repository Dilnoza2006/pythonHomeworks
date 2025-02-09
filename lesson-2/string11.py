string = input("Enter a string: ")
if any(char.isdigit() for char in string):
    print("The string contains digits.")
else:
    print("The string does not contain digits.")
