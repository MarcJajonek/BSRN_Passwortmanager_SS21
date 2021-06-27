#!/usr/bin/env python3

import string

def verschluesselung(usereingabe):
    liste = []
    # Kleinbuchstarben werden rausgesucht
    klein = string.ascii_lowercase
    # Grossbuchstareben werden rausgesucht
    gross = string.ascii_uppercase
    # Zahlen werden rausgesuch
    zahl = string.digits
    # Sonderzeichen werden rausgesuch
    zeichen = string.punctuation
    
    # Iteration durch den Text des users zur Verschlüsselung - Character für Character
    for i in range(len(usereingabe)):
        # Prüfung ob aktueller Character ein Kleinbuchstabe ist
        if usereingabe[i] in klein:
            index = klein.find(usereingabe[i])
            # Caesar-Verschlüsselung um einen bestimmten Wert
            umwandlung = klein[(index + 1)%26]
            liste.append(umwandlung)
        # Selbes für Grossbuchstabe 
        elif usereingabe[i] in gross:
            index = gross.find(usereingabe[i])
            umwandlung = gross[(index + 1)%26]
            liste.append(umwandlung)  
        # Selbes für Zahlen 
        elif usereingabe[i] in zahl:
            index = zahl.find(usereingabe[i])
            umwandlung = zahl[(index + 1)%10]
            liste.append(umwandlung) 
        # Selbes für Sonderzeichen 
        elif usereingabe[i] in zeichen:
            index = zeichen.find(usereingabe[i])
            umwandlung = zeichen[(index + 1)%26]
            liste.append(umwandlung) 
        else:
            liste.append(usereingabe[i])

    # Zusammensetzung der Verschlüsselung und Rückgabe 
    usereingabe = ''.join(liste[i] for i in range(len(liste)))
    return usereingabe

# Eine Funktion um verschlüsselte Werte wieder zu entschlüsseln 
def entschluesselung(usereingabe):
    liste = []
    # Kleinbuchstarben werden rausgesucht
    klein = string.ascii_lowercase
    # Grossbuchstareben werden rausgesucht
    gross = string.ascii_uppercase
    # Zahlen werden rausgesuch
    zahl = string.digits
    # Sonderzeichen werden rausgesuch
    zeichen = string.punctuation

    # Iteration durch den Text des users zur Entschlüsselung - Character für Character
    for i in range(len(usereingabe)):
        # Prüfung ob aktueller Character ein Kleinbuchstabe ist
        if usereingabe[i] in klein:
            index = klein.find(usereingabe[i])
            # Caesar-Entschlüsselung um einen bestimmten Wert
            umwandlung = klein[(index - 1)%26]
            liste.append(umwandlung)
        # Selbes für Grossbuchstabe 
        elif usereingabe[i] in gross:
            index = gross.find(usereingabe[i])
            umwandlung = gross[(index - 1)%26]
            liste.append(umwandlung) 
        # Selbes für Zahlen
        elif usereingabe[i] in zahl:
            index = zahl.find(usereingabe[i])
            umwandlung = zahl[(index - 1)%10]
            liste.append(umwandlung) 
        # Selbes für Sonderzeichen
        elif usereingabe[i] in zeichen:
            index = zeichen.find(usereingabe[i])
            umwandlung = zeichen[(index - 1)%26]
            liste.append(umwandlung) 
        else:
            liste.append(usereingabe[i])

    # Zusammensetzung der Entschlüsselung und Rückgabe 
    usereingabe = ''.join(liste[i] for i in range(len(liste)))
    return usereingabe