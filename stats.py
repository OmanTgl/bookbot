def count_words(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def count_char(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] =1
    return char_count


def sorted_dict(dict):
    sorted_list = []

    for char, count in dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list
