'''
Command Line Smart Interactive Dictionnary with a JSON Datafile  
'''
import json
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def find_definition (word):
    word = word.lower()
    if word in data :
        return data[word]
    elif len(get_close_matches(word.lower(), data.keys(), cutoff=0.5)) > 0 :
         alt = get_close_matches(word.lower(), data.keys(), cutoff=0.5)[0]
         yn = input(f"Did you mean {alt} instead ? Enter Y if Yes, N if No.")
         if yn == "Y" : 
             return data[get_close_matches(word.lower(), data.keys(), cutoff=0.5)[0]]
         elif yn =="N" : 
             return f"The word '{word}' doesn't exist in the dictionnary"
         else :
             return "Query Error - Answer unclear"
    else : 
        return f"The word '{word}' doesn't exist in the dictionnary"

word = input("Enter a word \n")

output = find_definition(word) 

if type(output) == list :
    for item in output : 
        print (item)
else : 
    print (output)