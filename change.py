#!/usr/bin/env python3

import getpass
from genpassword import genpassword
import sys
from datetime_check import datetime_check
from verentschluesselung import verschluesselung
from password import password





def change_Befehl():

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


    #Prüfung ob sich aktuelle anfrage in einem 30-Minütigem Zeitfenster befindet, in dem man nicht noch einmal das Master-Passwort eingeben muss
    datetime_check(text_arr)
    
    
    #Wenn title_arr leer ist soll eine Fehlermeldung ausgeben werden.
    if len(title_arr)  > 0:
        #Überprüfen ob das Kommando im Terminal in richtiger Syntax angeben wurde.
        if sys.argv[2] == "-title" and sys.argv[4] == "-generatepw" or sys.argv[4] == "-password":

            #Überprüfung ob Title in der Datei existiert
            if sys.argv[3] in title_arr:

                #Überprüfung ob Passwort generiert werden soll.
                if sys.argv[4] == "-generatepw":

                    

                    #Der folgende Code wird in einer try-except geschrieben, da er durch das abbrechen der Funktion genpassword() nicht die Variable gen_pw
                    #schreibt und somit der Fehler abgefangen wird.
                    try:
                        #Durch die Funktion genpassword() wird ein Passwort generiert, welches in die Variable gen_pw geschrieben wird.
                        gen_pw = genpassword()
                    
                        #Datei öffnen
                        b_file = open("pw_list.txt", "w")

                        j = 0
                        #Mittels Schleife soll das text_arr durchgegangen werden und die Stelle finden, an der der eingebene Title dem Title aus der Datei gleicht.
                        while j < anzahl:

                            if sys.argv[3] == text_arr[j]:
                                #Ändern des Passworts in das neue Passwort
                                text_arr[j+4] = verschluesselung(gen_pw)
                                k=0

                                #Mittels Schleife wird die Datei komplett neu geschrieben, somit wird die Änderung mitgenommen.
                                while k < anzahl:
                                    #Das letzte Leerzeichen soll damit wegfallen, da sonst die Datei falsch weitergeschrieben wird.
                                    if k == anzahl-1:
                                        b_file.write(text_arr[k])
                                        break
                                    else:
                                        b_file.write(text_arr[k]+" ")
                                    k += 1
                            j +=1
                    except UnboundLocalError:
                        print("Transaction cancelled pls try again!")
                
                #Wenn User das Passwort selber vergeben möchte
                elif sys.argv[4] == "-password":
                    password_var = getpass.getpass("Please enter your new password: \n")

                    #Aufrufen der Funktion password() und Übergabe der Eingabe aus dem Terminal
                    #In der Funktion wird das Passwort auf Sicherheit überprüft und nur wenn es sicher ist wird es gespeichert.
                    if password(password_var)== True:

                        #Datei öffnen
                        b_file = open("pw_list.txt", "w")
                        j = 0

                        #Mittels Schleife soll das text_arr durchgegangen werden und die Stelle finden, an der der eingebene Title dem Title aus der Datei gleicht.
                        while j < anzahl:
                            if sys.argv[3] == text_arr[j]:
                                #Ändern des Passworts in das neue Passwort
                                text_arr[j+4] = verschluesselung(password_var)
                                k=0

                                #Mittels Schleife wird die Datei komplett neu geschrieben, somit wird die Änderung mitgenommen.
                                while k < anzahl:
                                    #Das letzte Leerzeichen soll damit wegfallen, da sonst die Datei falsch weitergeschrieben wird.
                                    if k == anzahl-1:
                                        b_file.write(text_arr[k])
                                        break

                                    else:
                                        b_file.write(text_arr[k]+" ")

                                    k += 1
                            j +=1           

            #Wenn der eingegebene Title nicht im title_arr, dann Fehlermeldung.
            else:
                print("There is no title with this name!")
                
        #Ausgabe wenn der User den Befehl falsch eingegeben hat
        else:
            print("Please enter your command in correct Syntax!\n"
            "Call Function help, if you need an example")        

    #Ausgabe wenn der es noch keinen Title gibt
    else:
        print("There is no title yet!")