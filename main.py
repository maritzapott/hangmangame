import requests
import json

authenticate = requests.get('https://random-words-api.vercel.app/word')
randomwords = authenticate.json()

def _choose_word():
    for item in randomwords:
        return item['word'].lower()



def _hint(word):
    '''Returns the definition of the random word'''
    for item in randomwords:
        return item['definition']




