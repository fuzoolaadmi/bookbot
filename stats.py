def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on_num(item):
    return item["num"]


def sort_chars(chars_dict):
    chars_list = []
    for ch, count in chars_dict.items():
        chars_list.append({"char": ch, "num": count})

    chars_list.sort(key=sort_on_num, reverse=True)
    return chars_list
