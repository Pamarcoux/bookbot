def count_words(contents):
    num_words = len(contents.split())
    return(num_words)

def count_character(contents):
    character = {}
    contents_lower = contents.lower()
    for letter in contents_lower:
        if letter not in character:
            character[letter] = 1
        else:
            character[letter]+=1
    return(character)

def sort_on(items):
    return items["num"]

def sort_character(characters):
    list_dict = []
    for character in characters:
        char_dict = {
                "char":"",
                "num":0
                }
        char_dict["char"] = character
        char_dict["num"] = characters[character]
        list_dict.append(char_dict)
    list_dict.sort(reverse=True, key=sort_on)
    return(list_dict)

