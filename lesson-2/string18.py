string = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")

if string.startswith(start_word) and string.endswith(end_word):
    print("The string starts and ends as specified.")
else:
    print("The string does not match the start or end criteria.")