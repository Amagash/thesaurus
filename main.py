import json
from difflib import SequenceMatcher, get_close_matches
import mysql.connector

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        definitions = data[word]
        return definitions[0]
    elif get_close_matches(word, data):
        closest_match = get_close_matches(word, data)[0]
        answer = input ("The word {} doesn't exist. Did you mean %s ? Enter Y if yes, or N if no: ".format(word) % get_close_matches(word, data)[0])
        if answer == "Y":
            return data[closest_match][0]
        elif answer == "N":
            "The word was not found"
        else: 
            print ("I did not understand your entry")
    else:
        return "The word was not found"



if __name__ == "__main__":
    con = mysql.connector.connect(user='ardit700_student', password='ardit700_student', host='108.167.140.122', database='ardit700_pm1database')
    cursor = con.cursor()
    query = cursor.execute("SELECT * FROM Dictionary")
    results = cursor.fetchall()
    print(type(results))
    
    # word = input("input word: ")
    # print(word)
    # print(translate(word))