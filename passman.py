#!/usr/bin/env python3
import sys
from copy_befehl import copy_Befehl
from add import add_Befehl
from delete import delete_Befehl
from change import change_Befehl
from table import table_Befehl
from checks_befehl import check_Befehl
from help_befehl import help_Befehl
from change_mp import change_mp


#help_Befehl wird aufgerufen wenn User help übergibt
if sys.argv[1] == "help":
    help_Befehl()

else:

    try:
        check_Befehl()

        #An Hand der vom Nutzer eingegebenen Parameter wird entschieden, welche Methode aufegrufen 
        #Add_Befehl wird aufgerufen wenn User add übergibt
        if sys.argv[1] == "add":
            add_Befehl()
        #delete_Befehl wird aufgerufen wenn User delete übergibt
        elif sys.argv[1] == "delete":
            delete_Befehl()
        #change_Befehl wird aufgerufen wenn User change übergibt 
        elif sys.argv[1] == "change":
            change_Befehl()
        #table_Befehl wird aufgerufen wenn User table übergibt
        elif sys.argv[1] == "table":
            table_Befehl()
        #copy_Befehl wird aufgerufen wenn User copy übergibt
        elif sys.argv[1] == "copy":
            copy_Befehl()
        #changemp wird aufgerufen wenn User changemp übergibt
        elif sys.argv[1] == "changemp":
            change_mp()
    #KeyboardInterrupt bei Strg+C       
    except KeyboardInterrupt:
        print("Transaction canceled!")
        sys.exit()
    #IndexError bei zu kurzer Eingabe eines Befehls
    except IndexError:
            print("Please enter your command in correct Syntax!\n"
                "Call Function help, if you need an example")