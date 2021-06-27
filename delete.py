#!/usr/bin/env python3
import sys
from datetime_check import datetime_check

def delete_Befehl():

    #Datei öffnen und Daten in eine List schreiben, getrennt wird durch ein Leerzeichen.
    #Definieren von variablen
    text_file = open("pw_list.txt").read()
    text_arr  = text_file.split(" ")
    anzahl = len(text_arr)

    i = 0
    title_arr = []

    # Die Einträge nach einem "-title" in eine List eintargen - somit sind alle titles in einer List
    while i < anzahl:
        if text_arr[i] == "-title":
            title_arr.append(text_arr[i+1])
        i += 1

    #Prüfung ob sich aktuelle anfrage in einem 30-Minütigem Zeitfenster befindet, in dem man nicht noch einmal das Master-Passwort eingeben muss
    datetime_check(text_arr)

    #Überprüfung ob Kommando im Terminal richtig eingegeben wurde. Wenn nicht Fehlerrückmeldung ausgeben
    if sys.argv[2] == "-title":
        #Überprüfung ob eingegebener Title im Title_arr ist
        if sys.argv[3] in title_arr:
            
            i = 0  
            #Mittels Schleife soll die Stelle gefunden werden, an der der eingegebene Title und der Title aus der Datei übereinstimmen.
            while i < anzahl:
                if sys.argv[3] == text_arr[i]:
                    #erneute Abfrage, ob Einträge wirklich gelöscht werden sollen.
                    löschen = input("Do you want to delete the password ? (y/n)\n")
                    
                    #Wenn ja, dann wird der komplette Eintrag zum eingegebenen Title gelöscht
                    if löschen == "y":
                        text_arr.pop(i+5)
                        text_arr.pop(i+4)
                        text_arr.pop(i+3)
                        text_arr.pop(i+2)
                        text_arr.pop(i+1)
                        text_arr.pop(i) 
                        text_arr.pop(i-1)                   
                        
                        #Datei öffnen
                        a_file = open("pw_list.txt", "w")

                        
                        j = 0

                        #Mittels Schleife wird die Datei komplett neugeschrieben, ohne die gelöschten Elemente
                        while j < anzahl:
                            
                            #Das letzte \n soll damit wegfallen, da sonst die Datei falsch weitergeschrieben wird.
                            if j == len(text_arr)-1:
                                a_file.write(text_arr[j])
                                break
                                
                                
                            else:
                                a_file.write(text_arr[j]+" ")
                                

                            j += 1
                        
                        a_file.close()
                        break
                        
                    else:
                        print("Transaction was canceled")
                        break
                i += 1
        else:
            print("There is no entry for title " + sys.argv[3]) 
         
    else:
        print("Please enter your command in correct Syntax!\n"
        "Call Function help, if you need an example")

