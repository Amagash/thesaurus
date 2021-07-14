import json
from difflib import SequenceMatcher, get_close_matches

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        matches = get_close_matches(word, data)
        return "The word {} doesn't exist. Did you mean {}?".format(word, matches[0])

# def best_similarity(data, word):
#     word = word.lower()
#     best_ratio = 0
#     best_match = ""
#     for item in data:
#         match = SequenceMatcher(None, word, item).ratio()
#         if match > best_ratio:
#             best_ratio = match
#             best_match = item
#     print (best_match, best_ratio)


data = json.load(open("data.json"))
word = 'rainn'
# word = input("input word: ")

print(translate(word))
