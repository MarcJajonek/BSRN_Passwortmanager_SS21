#!/usr/bin/env python3
import string
import random


def genpassword():
    #Try except Error abfangen, der beim Input bei der Länge durch das Eingeben eines Zeichens, welches keine Zahl ist, entsteht   
    try:
        #Eingabe der Passwortlänge
        pw_lenght = int(input("Please enter the length your password should be:\n"))
        
        #Überprüfen ob Passwort länge mindestens 8 Zeichen lang ist 
        if pw_lenght < 8:  
            print("The password must have atleast a length of 8 characters.")

        
        else:
            #Abfrage welche Zeichen im Passwort enthalten sein sollen.
            small_bool = input("Should your password contain small letters? (y/n)\n")
            if small_bool == "y":
                small_num = 1
            else:
                small_num = 0
            capital_bool = input("Should your password contain capital letters? (y/n)\n")
            if capital_bool  == "y":
                capital_num = 1
            else: 
                capital_num = 0
            symbol_bool = input("Should your password contain symbols? (y/n)\n")
            if symbol_bool == "y":
                symbol_num = 1
            else:
                symbol_num = 0
            num_bool = input("Should your password contain numbers? (y/n)\n")
            if num_bool == "y":
                num_num = 1
            else: 
                num_num = 0

            all = ""
            
            secruity = num_num + symbol_num + capital_num + small_num
            

            #Abfangen der Option, falls alles mit nein beantwortet wurde.
            if small_bool != "y" and capital_bool != "y" and symbol_bool != "y" and num_bool != "y":
                print("Your password must contain something!")

            elif secruity < 3:
                print("Make sure you password contain at least 3 different character types")
                
            else:
                #Wenn diese Zeichen enthalten werden sollen, werden diese an ein Array hinzugefügt
                if small_bool == "y":
                    lower = string.ascii_lowercase
                    all += lower

                else:
                    pass

                if capital_bool == "y":

                    upper = string.ascii_uppercase
                    all = all + upper 
                
                else: 
                    pass

                if symbol_bool == "y":

                    symbols = string.punctuation
                    all = all + symbols
                
                else: 
                    pass

                if num_bool == "y":

                    num = string.digits
                    all = all + num

                else:
                    pass
                
                #Zufällige Kombination aus den Vorhandenen Zeichen zusammenstellen, mit der Länge die angegeben wurde.
                temp = random.sample(all,pw_lenght)

                #Variable fertigstellen
                gen_pw = "".join(temp)

    except ValueError:
        print("Please enter an Integer")
    
    #Rückgabe des Passwortes
    return gen_pw