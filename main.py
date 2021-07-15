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

def connection_to_db():
    mydb = mysql.connector.connect(
        host = "108.167.140.122",
        user = "ardit700_student",
        passwd = "ardit700_student",
        database = "ardit700_pm1database"
    )

    return mydb

    
def get_result(word, cursor):
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    word = input("input word: ")
    mydb = connection_to_db()
    cursor = mydb.cursor()
    results = get_result(word, cursor)
    print(results)

    # get_result(word)
    
    
    # print(word)
    # print(translate(word))