import json
from difflib import SequenceMatcher, get_close_matches

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word, data):
        closest_match = get_close_matches(word, data)[0]
        answer = input ("The word {} doesn't exist. Did you mean %s ? Enter Y if yes, or N if no: ".format(word) % get_close_matches(word, data)[0])
        if answer == "Y":
            return data[closest_match]
        elif answer == "N":
            "The word was not found"
        else: 
            print ("I did not understand your entry")
    else:
        return "The word was not found"

data = json.load(open("data.json"))
word = 'rainn'
# word = input("input word: ")

print(translate(word))
