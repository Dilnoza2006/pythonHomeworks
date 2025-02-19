import os
import string
from collections import Counter

def create_sample_file():
    """Create sample.txt if it doesn't exist."""
    if not os.path.exists("sample.txt"):
        print("File 'sample.txt' not found. Please create it by typing a paragraph below:")
        user_input = input("Type your paragraph: ")
        with open("sample.txt", "w") as file:
            file.write(user_input)
        print("File 'sample.txt' created successfully.")

def clean_word(word):
    """Remove punctuation and convert to lowercase."""
    return word.strip(string.punctuation).lower()

def count_word_frequency(file_path):
    """Count the frequency of each word in the file."""
    with open(file_path, "r") as file:
        text = file.read()
    words = text.split()
    cleaned_words = [clean_word(word) for word in words]
    word_count = Counter(cleaned_words)
    return word_count

def save_report(total_words, top_words, top_n):
    """Save the word count report to a file."""
    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            report_file.write(f"{word} - {count}\n")

def main():
    # Step 1: Ensure sample.txt exists
    create_sample_file()

    # Step 2: Count word frequency
    word_count = count_word_frequency("sample.txt")
    total_words = sum(word_count.values())

    # Step 3: Ask user for the number of top words to display
    try:
        top_n = int(input("How many top common words would you like to display? "))
    except ValueError:
        print("Invalid input. Defaulting to top 5 words.")
        top_n = 5

    # Step 4: Get the top N words
    top_words = word_count.most_common(top_n)

    # Step 5: Display results
    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    # Step 6: Save the report
    save_report(total_words, top_words, top_n)
    print("\nReport saved to 'word_count_report.txt'.")

if __name__ == "__main__":
    main()