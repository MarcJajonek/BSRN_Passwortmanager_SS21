#!/usr/bin/env python3

import datetime
import sys
from verentschluesselung import entschluesselung
import pyperclip
from datetime import timedelta
from datetime_check import datetime_check
import getpass





def copy_Befehl():
     
    #Masterpasswort einlesen
    text_file = open("pw_list.txt").read()
    text_arr = text_file.split(" ")
    i = 0

    while i < len(text_arr):
        if text_arr[i] == "MasterPassword":
            masterpw = text_arr[i + 1]
        i += 1

    # Input bis Passwort richtig ist, Passwort wird durch getpass Funktion nicht angezeigt
    input_masterpw = getpass.getpass("Enter Master-Passwort: ")
    while entschluesselung(masterpw) != input_masterpw:
        input_masterpw = getpass.getpass("Wrong Master-Passwort, try again: ")
    print("Master-Passwort Ok!")

    #Titel, passwort und Username in Array einlesen
    data_arr = []
    c = 0
    while c < len(text_arr):
        if text_arr[c] == "-title":
            data_arr.append(text_arr[c + 1])
        elif text_arr[c] == "-password":
            data_arr.append(text_arr[c + 1])
        elif text_arr[c] == "-username":
            data_arr.append(text_arr[c + 1])
        c += 1

    #Input Title
    #Überprüfen ob eingegebner Title vorhanden ist,
    #username wird dann ausgegeben und passwort für 30 sec in clipboard gespeichert
    if sys.argv[2] == "-title":
        if sys.argv[3] in data_arr:
            title_pos = data_arr.index(sys.argv[3])
            # Username befindet sich im Array an der Position nach Title
            print("Username: " + data_arr[title_pos + 1] + " | password copied to clipboard")
            start = datetime.datetime.now()

            # nicht länger als 30 sec in Clipboard speichern
            while (timedelta.total_seconds(datetime.datetime.now() - start)) <= 30:
                # Passwort befindet sich im Array zwei Positionen nach Title
                pyperclip.copy(entschluesselung(data_arr[title_pos + 2]))
            pyperclip.copy("")
            print("30 sec are over, deleted password from clipboard!")
        else:
            print("Title doesn't exist")
            
    else:
        print("Please enter your command in correct Syntax!\n"
            "Call Function help, if you need an example")