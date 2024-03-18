import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def get_definition(word):
    
    word = word.lower()

    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) != 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return ("The word doesn't exist, yet.")

word_user = input("Enter a word: ")
output = get_definition(word_user)

if type(output) == list:
    for item in output:
        print("-",item)

else:
    print("-",output)
