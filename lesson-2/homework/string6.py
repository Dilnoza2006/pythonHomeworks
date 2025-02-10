def contains(sub, main):
    return sub in main

main_string = input("Enter main string: ")
sub_string = input("Enter substring: ")

if contains(sub_string, main_string):
    print("Substring found!")
else:
    print("Substring not found!")