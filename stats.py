def count_words(book_text):
    return len(book_text.split())

def character_count(book_text):
    character_count = {}
    for i in book_text:
        lowered = i.lower()
        if lowered not in character_count:
            character_count[lowered] = 1
        else:
            character_count[lowered] += 1
    return character_count

def sort_dictionary(unsorted):
    sorted = []
    for entry in unsorted:
        sorted.append({'character': entry, 'count': unsorted[entry]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def sort_on(dict):
    return dict['count']
