#!/usr/bin/env python3
from datetime_check import datetime_check


def table_Befehl():
    text_file = open("pw_list.txt").read()
    text_arr  = text_file.split(" ")
    anzahl = len(text_arr)

    #Prüfung ob sich aktuelle anfrage in einem 30-Minütigem Zeitfenster befindet, in dem man nicht noch einmal das Master-Passwort eingeben muss
    datetime_check(text_arr)

    #Text Tabellenkopf
    header = ['Title', 'Username']

    #Daten einlesen
    text_file = open("pw_list.txt").read()
    text_arr = text_file.split(" ")
    anzahl = len(text_arr)

    i = 0
    tabledata_arr =[]

    #Title und username in Array einlesen
    while i < anzahl:
        if text_arr[i] == "-title":
            tabledata_arr.append(text_arr[i + 1])
        elif text_arr[i] == "-username":
            tabledata_arr.append(text_arr[i + 1])
        i += 1

    #Array teilen in größe 2
    splitdata_arr = [
        tabledata_arr[z:z +2]
        for z in range(0,len(tabledata_arr), 2)
    ]

    #Formatierung der Tabellenspalten
    def fixed_lenght(text,lenght):
        if len(text) > lenght:
            text = text[:lenght]
        elif len(text) < lenght:
            text = (text + " " * lenght) [:lenght]
        return text

    #Tabellenkopf ausgeben
    print("| ", end=" ")
    for column in header:
        print (fixed_lenght(column,20), end = " | ")
    print()
    print("-"*48)

    #Daten in Tabelle ausgeben
    for row in splitdata_arr:
        print("| ", end=" ")
        for column in row:
            print(fixed_lenght(column,20), end = " | ")
        print()
        print("-"*48)