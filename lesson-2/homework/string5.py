def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count

string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(string)
print(f"Vowels: {vowels}, Consonants: {consonants}")