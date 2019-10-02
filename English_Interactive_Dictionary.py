"""
Pmk
English Interactive Dictionary
"""

import os
import json
import difflib

os.getcwd()
os.chdir(r'D:\Github_Projects\10 Apps\Interactive_English_Dictionary'.replace(os.sep , os.altsep))
data = json.load(open('data.json'))


def keydefinition(key):
    if key.lower() in data.keys():
        return data[key]
    else:
        if difflib.get_close_matches(key.lower(), data.keys(), cutoff=0.8) != []:
            similar = difflib.get_close_matches(key.lower(), data.keys(), cutoff=0.8)[0].capitalize()
            comfirmation = input(f"This dictionary doesn't contain word '{key}'. Did you mean '{similar}'? Please write Y if yes, or N if no.\n[Y]/[N]: ")
            while comfirmation not in ['Y', 'N']:
                comfirmation = input('Please enter capitalized Y or N: ')
            if comfirmation == 'Y':
                return data[similar.lower()]
            else:
                return 'Thank you for using my dictionary.'
        else:
            return 'This dictionary does not contain such word or similar to it.'



key = input('Enter a word you would like to translate: ')

keydefinition(key)

if isinstance(keydefinition(key), list):
    print(key.capitalize() + ':')
    for i in keydefinition(key):
        print('\n' + i)
else:
    print(keydefinition(key))
    






































def keydefinition(key):
    if key.lower() in data.keys():
        print(key.capitalize() + ':')
        for i in data[key]:
            print('\n' + i)
    else:
        similar = difflib.get_close_matches(key, data.keys(), cutoff=0.8)
        if similar != []:
            similar = similar[0].capitalize()
            confirmation = input(f"This dictionary doesn't contain word '{key}'. Did you mean '{similar}'? Please write Y if yes, or N if no.\n[Y]/[N]: ")
            while confirmation not in ['Y', 'N']:
                confirmation = input(f"Please enter capitalized Y or N: ")
            if confirmation == 'Y':
                print(similar.capitalize() + ':')
                for i in data[similar.lower()]:
                    print('\n' + i)
            else:
                print('Thank you for using my dictionary.')
        else:
            print('This dictionary does not contain such word or similar to it.')