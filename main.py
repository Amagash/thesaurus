import json


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist."


data = json.load(open("data.json"))
word = input("input word: ")

print(translate(word))