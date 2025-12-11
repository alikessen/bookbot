def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_chars_dict(text):
    text = text.lower()
    dict = {}

    for c in text:
        dict[c] = dict.get(c, 0) + 1
     
    return dict

def create_report(char_dict):
    char_list = []

    for key, value in char_dict.items():
        small_dict = {"char": key, "num": value}
        char_list.append(small_dict)

    char_list.sort(reverse=True, key=sort_on_num)

    return char_list

def sort_on_num(item):
    return item["num"]