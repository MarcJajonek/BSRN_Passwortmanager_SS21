#!/usr/bin/env python3
import getpass
from pathlib import Path
import os
import re
from verentschluesselung import verschluesselung
import datetime




def check_Befehl():
    # Nutzernamen in variable Speichern
    user = getpass.getuser()
    # Ordner in den die PWList gespeichert werden soll in variable speichern
    ordner = Path("./.passman")

    file = Path("./pw_list.txt")
    # zum Verzeichnis springen in den der Ordner erzeugt werden soll.
    os.chdir('/home/'+user)

    # Abfrage ob vorher PWManager vorher schonmal benutzt, wenn nicht dann soll der Ordner angelegt werden.
    if ordner.is_dir():
        os.chdir('./.passman')
        #Abfrage ob Datei existiert 
        if file.is_file():

            #Wenn ja dann soll die Datei geöffnet werden und die Daten in eine Liste gespeichert werden
            text_file = open("pw_list.txt").read()
            text_arr  = text_file.split(" ")

        else:
            #Wenn nein soll die Datei erstellt werden. Danach soll die Datei geöffnet werden und die Daten
            #in eine Liste gespeichert werden.
            os.system("touch pw_list.txt")
            text_file = open("pw_list.txt").read()
            text_arr  = text_file.split(" ")


        #Fehlerausgrenzung beim falschen schreiben der Datei. 
        #Wenn die Anzahl der Daten in der Liste kleiner 4 ist soll nochmal das MP vergeben werden.
        if len(text_arr) < 4:

            datei = open('pw_list.txt', 'w')
            datei.write(" MasterPassword ")
            mp = getpass.getpass("Please set a master password:\n")

            # Prüfung ob Master-Passwort sicher genug ist
            while True:
                if len(mp) < 8:
                    print("Make sure your password is at least 8 characters.")
                    mp = getpass.getpass("Please set a master password:\n")
                elif re.search('[0-9]', mp) is None:
                    print("Make sure your password has a number in it.")
                    mp = getpass.getpass("Please set a master password:\n")
                elif re.search('[A-Z]', mp) is None:
                    print("Make sure your password has a capital letter in it.")
                    mp = getpass.getpass("Please set a master password:\n")
                elif re.search('[a-z]', mp) is None:
                    print("Make sure your password has a small letter in it.")
                    mp = getpass.getpass("Please set a master password:\n")
                elif re.search('[!-/]', mp) is None:
                    print("Make sure your password has a symbol in it.")
                    mp = getpass.getpass("Please set a master password:\n")
                else:
                    datei.write(verschluesselung(mp) + " " + "\n")
                    break

            #Aktuelle Zeit wird in Datei geschrieben
            datei.write(" Zeit " + str(datetime.datetime.now()) + " " + "\n")
            datei.close()
    
    #Wenn der Ordner noch nicht erstellt wurde, soll dieser angelegt werden und die Datei im Anschluss        
    else:
        os.system("mkdir .passman")
        os.chdir('./.passman')
        os.system("touch pw_list.txt")

        # Aufforderrung des Nutzers ein Master-Passwort anzulegen. Dieses wird dann verschlüsselt und in der Datei gespeichert
        datei = open('pw_list.txt', 'a')
        datei.write(" MasterPassword ")
        mp = getpass.getpass("Please set a master password:\n")

        # Prüfung ob Master-Passwort sicher genug ist
        while True:
            if len(mp) < 8:
                print("Make sure your password is at least 8 characters.")
                mp = getpass.getpass("Please set a master password:\n")
            elif re.search('[0-9]', mp) is None:
                print("Make sure your password has a number in it.")
                mp = getpass.getpass("Please set a master password:\n")
            elif re.search('[A-Z]', mp) is None:
                print("Make sure your password has a capital letter in it.")
                mp = getpass.getpass("Please set a master password:\n")
            elif re.search('[a-z]', mp) is None:
                print("Make sure your password has a small letter in it.")
                mp = getpass.getpass("Please set a master password:\n")
            elif re.search('[!-/]', mp) is None:
                print("Make sure your password has a symbol in it.")
                mp = getpass.getpass("Please set a master password:\n")
            else:
                datei.write(verschluesselung(mp) + " " + "\n")
                break

        

        # Aktuelle Zeit wird in Datei geschrieben
        datei.write(" Zeit " + str(datetime.datetime.now()) + " " + "\n")
        datei.close()