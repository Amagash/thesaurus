import json
from difflib import SequenceMatcher

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist."

def best_similarity(data, word):
    word = word.lower()
    best_ratio = 0
    best_match = ""
    for item in data:
        match = SequenceMatcher(None, word, item).ratio()
        if match > best_ratio:
            best_ratio = match
            best_match = item
    print (best_match, best_ratio)


data = json.load(open("data.json"))
word = 'rainn'
# word = input("input word: ")

# print(translate(word))

best_similarity(data, word)