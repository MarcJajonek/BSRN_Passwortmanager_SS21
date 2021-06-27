#!/usr/bin/env python3
import re

def password(password):

    #Überprüfung ob das Passwort min. 8 Zeichen lang ist.
    if len(password) < 8:
        print("Make sure your password is at least 8 characters.")
    #Überprüfen ob das Passwort Zahlen beinhaltet
    elif re.search('[0-9]', password) is None:
        print("Make sure your password has a number in it.")
    #Überprüfen ob das Passwort Großbuchstaben beinhaltet
    elif re.search('[A-Z]', password) is None:
        print("Make sure your password has a capital letter in it.")
    #Überprüfen ob das Passwort Kleinbuchstaben beinhaltet
    elif re.search('[a-z]', password) is None:
        print("Make sure your password has a small letter in it.")
    #Überprüfen ob das Passwort Symbole beinhaltet
    elif re.search('[!-/]', password) is None:
        print("Make sure your password has a symbol in it.")
    #Wenn alles drin ist wird True zurückgegeben.    
    else:
        return True