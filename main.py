def count_character(text):
    counter = {}
    for c in text.lower():
        if c.isalpha():
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
    return counter

def count_words(text):
    words = text.split()
    return len(words)

def sort_on(item):
    return item['count']

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document")
        char_counts = []
        char_dict = count_character(file_contents)
        for char in char_dict:
            char_counts.append({ 'char': char, 'count': char_dict[char]})
        char_counts.sort(reverse=True, key=sort_on)
        for char_count_dict in char_counts:
            print(f"The '{char_count_dict['char']}' character was found {char_count_dict['count']} times")
        print("--- End report ---")

main()