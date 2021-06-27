#!/usr/bin/env python3

import getpass
import sys 
from verentschluesselung import verschluesselung
from datetime_check import datetime_check
from password import password
from genpassword import genpassword


def add_Befehl():

    #Datei öffnen und Daten in eine List schreiben, getrennt wird durch ein Leerzeichen.
    #Definieren von variablen
    text_file = open("pw_list.txt").read()
    text_arr  = text_file.split(" ")
    anzahl = len(text_arr)


    i = 0
    title_arr = []

    #Die Einträge nach einem "-title" in eine List eintragen - somit sind alle titles in einer List
    while i < anzahl:
        if text_arr[i] == "-title":
            title_arr.append(text_arr[i+1])
        i += 1

    # Einlesen der Kommandos im Terminal und speichern im sys.argv[]
    num_arguments = len(sys.argv[1:])

    #Prüfung ob sich aktuelle Anfrage in einem 30-Minütigem Zeitfenster befindet, in dem man nicht noch einmal das Master-Passwort eingeben muss
    datetime_check(text_arr)

    #Überprüfung ob Kommando im Terminal richtig eingegeben wurde. Wenn nicht Fehlerrückmeldung ausgeben
    if sys.argv[2] == "-title" and sys.argv[4] == "-username" and sys.argv[6] == "-generatepw" or sys.argv[6] == "-password": 
        #Überprüfen ob das Passwort generiert werden soll, wenn nicht wird Passwort selbst angegeben.
        if sys.argv[6] == "-generatepw":
            #Überprüfung ob der angegebene Title in der Datei und somit schom im title_arr ist.
            if sys.argv[3] in title_arr:
                    print("There is a password for this title. Please enter a new title or change the password.")

            else:
                        #Der folgende Code wird in einer try-except geschrieben, da er durch das abbrechen der Funktion genpassword() nicht die Variable gen_pw
                        #schreibt und somit der Fehler abgefangen wird.
                        try:
                            #Durch die Funktion genpassword() wird ein Passwort generiert, welches in die Variable gen_pw geschrieben wird.
                            gen_pw = genpassword()

                            #Datei öffnen und Angaben in korrekter Syntax hinzufügen.
                            datei = open('pw_list.txt', 'a')
                            datei.write(" ")
                            i = 2
                            while i <= num_arguments-1:
                                datei.write(sys.argv[i] + " ")
                                i=i+1
                            datei.write("-password ")
                            datei.write(verschluesselung(gen_pw))
                            datei.write(" \n")
                            datei.close()
                        except UnboundLocalError:
                                print("Transaction cancelled pls try again!")                        

        #Danach wird das Passwort auf sicherheit geprüft. Bei fehlenden Angaben, wird eine Fehlermeldung ausgegeben.
        #Wenn alles passt wird der Eintrag in der Datei erzeugt.   
        else:
            #Überprüfung ob der angegebene Title in der Datei und somit schom im title_arr ist.
            if sys.argv[3] in title_arr:
                print("There is a password for this title. Please enter a new title or change the password.")

            else:
                password_var = getpass.getpass("Please enter your password: \n")
                #Aufrufen der Funktion password() und Übergabe der Eingabe aus dem Terminal
                #In der Funktion wird das Passwort auf Sicherheit überprüft und nur wenn es sicher ist wird es gespeichert.
                if password(password_var) == True: 
                    
                    #Datei öffnen und Angaben in korrekter Syntax hinzufügen. 
                    datei = open('pw_list.txt', 'a')
                    datei.write(" ")
                    i = 2
                    while i <= num_arguments+1:
                        if i > num_arguments:
                            datei.write(verschluesselung(password_var))
                        else:
                            datei.write((sys.argv[i]) + " ")
                        i=i+1
                    
                    datei.write(" \n")
                    datei.close()

    else: 
        print("Please enter your command in correct Syntax!\n"
        "Call Function help, if you need an example")