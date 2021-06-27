#!/usr/bin/env python3

import getpass
from password import password
from datetime_check import datetime_check
import sys
from verentschluesselung import verschluesselung
from password import password

def change_mp():


    # Datei öffnen und Daten in eine List schreiben, getrennt wird durch ein Leerzeichen.
    # Definieren von variablen
    text_file = open("pw_list.txt").read()
    text_arr  = text_file.split(" ")
    anzahl = len(text_arr)


    # Prüfung ob sich aktuelle anfrage in einem 30-Minütigem Zeitfenster befindet, in dem man nicht noch einmal das Master-Passwort eingeben muss
    datetime_check(text_arr)
    
    if sys.argv[2] == "-password":
        password_var = getpass.getpass("Please enter your new master-password: \n")
        # Prüft ob das eingegebene Password sicher genug ist und unseren standards entspricht 
        if password(password_var) == True:
            i = 0 
            while i < anzahl:
                if text_arr[i] == "MasterPassword":
                    text_arr[i+1] = verschluesselung(password_var)
                    
                # Neuschreiben der Liste
                k = 0 
                a_file = open("pw_list.txt", "w")
                while k < anzahl:
                    if k == anzahl-1:
                        a_file.write(text_arr[k])
                        break
                    else:
                        a_file.write(text_arr[k] + " ")
                    k +=1 
                i += 1
    # Syntax Überprüfung
    else:
        print("Please enter your command in correct Syntax!\n"
        "Call Function help, if you need an example")
