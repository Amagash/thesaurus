import json
from difflib import SequenceMatcher, get_close_matches

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word, data):
        return "The word {} doesn't exist. Did you mean %s ?".format(word) % get_close_matches(word, data)[0]
    else:
        return "The word was not found"

data = json.load(open("data.json"))
word = 'rain'
# word = input("input word: ")

print(translate(word))
