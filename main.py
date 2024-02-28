def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    char_count_sort(char_counter(text))
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def char_counter(text):
    lowered_text = text.lower()
    chars = {}
    for char in lowered_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def char_count_sort(char_count):
    sorted_chars = (sorted(char_count.items(), key=lambda char: char[1], reverse=True))
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"The {char[0]} character was found {char[1]} times")

main()