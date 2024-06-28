def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list_of_dicts = convert_chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, chars_list_of_dicts, num_words)

def print_report(book_path, chars_list_of_dicts, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document")
    print()

    for item in chars_list_of_dicts:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def convert_chars_dict_to_sorted_list(chars_dict):
    list_of_dicts = []
    for ch in chars_dict:
        list_of_dicts.append({'char':ch, "num":chars_dict[ch]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars 

def get_num_words(string):
    return len(string.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()