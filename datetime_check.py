#!/usr/bin/env python3
import datetime
from verentschluesselung import verschluesselung
import getpass

def datetime_check(text_arr):
    
    i = 0
    j = 0
    k = 0

    #Ermittlung des Datums(datum_datei) und der Zeit(zeit_datei) anhand der gespeicherten Daten im Dokument 
    while i < len(text_arr):
        if text_arr[i] == "Zeit":
            datum_datei = text_arr[i+1]
            zeit_datei = text_arr[i+2]
        i += 1

    # Deklaration wichtiger Variablen zur Berechnung der Zeit
    datum_now = datetime.date.today()
    zeit_now = datetime.datetime.now().time()
    # Zeit aus der Datei wird vom Datentyp "String" in ein Datentyp "datetime" konvertiert
    zeit_format_datei = datetime.datetime.strptime(zeit_datei, '%H:%M:%S.%f')
    zeit_format_now = datetime.datetime.strptime(str(zeit_now), '%H:%M:%S.%f')
    # Differenzbildung der aktuellen Zeit und der Zeit, die im Dokument hinterlegt ist
    zeit_diff = zeit_format_now - zeit_format_datei

    # Abfrage ob Datum in der Datei identisch ist und ob die Zeitliche 
    # differenz zwischen "Aktuell" und "Datei" kleiner ist als 5 Minuten (300 Sekunden)
    if str(datum_datei) == str(datum_now) and (zeit_diff.seconds <= 300):
        # Wenn das Datum übereinstimmt und man sich im Zeitlichen Rahmen von 5 Minuten befindet,
        #  wird noch abgefragt, ob die bereits vergangene Zeit groesser als 3 Minten ist (180 Sekunden)
        if zeit_diff.seconds >= 180:
            # Wenn man nur noch 3 Minten oder weniger zeit hat, 
            # wird die Volle Minute zusammen mit einem Text ausgegeben, der besagt, wie viel zeit man 
            # noch hat, bis man das Passwort wieder erneut eingeben muss
            zeit_diff_minute = round((300 - zeit_diff.seconds) / 60)
            print("You have " + str(zeit_diff_minute) + " minutes left")
        else:
            print("Master password: OK")

    # Wenn man sich auserhalb des 5 Minuten Zeitrahmens befindet, wird der Nutzer aufgefordert sein Passwort erneut einzugeben        
    else:            
        masterPW = getpass.getpass("Please enter your master password: \n")
        datei = open('pw_list.txt', 'r')

        # Suche nach dem Master-Passwort in der Datei
        while j < len(text_arr):
            if text_arr[j] == "MasterPassword":
                master_pw_datei = text_arr[j+1]
                
            # Suche nach der Zeit & Datum in der Datei, um diese später überschreiben zu können
            if text_arr[j] == "Zeit":
                text_arr[j+1] = str(datum_now)
                text_arr[j+2] = str(zeit_now)

                # Abfrage ob das vom Nuter eingegebene Passwort indentisch mit dem Master-Passwort in der Datei ist
                if master_pw_datei == (verschluesselung(masterPW)):
                    datei.close()
                    datei = open('pw_list.txt', 'w')

                    #Überschreiben der Zeit mit dem aktuellen Datum und der aktuellen Urzeit 
                    while k < len(text_arr):
                        if text_arr[k] == "Zeit":
                            datei.write("Zeit ")
                            datei.write(str(text_arr[k+1]+" "))
                            datei.write(str(text_arr[k+2]+ " "))
                            k +=2
                        #Alle anderen in der Datei verhandenen informationen werden auch neu geschrieben, da sie sonst gelöscht werden würden
                        else:
                            datei.write(text_arr[k]+" ")
                        k += 1

                # Wenn sich das vom Nuter eingegebenes Passwort von dem Master-Passwort in der Datei unterscheidet, wird so lange nach dem richtigen
                # gefragt, bis es gefunden wurde
                while (verschluesselung(masterPW)) != master_pw_datei:
                    masterPW = getpass.getpass("Password was incorrect. Please enter yor password:\n")

                     # Abfrage ob das vom Nuter eingegebene Passwort indentisch mit dem Master-Passwort in der Datei ist
                    if master_pw_datei == (verschluesselung(masterPW)):
                        datei.close()
                        datei = open('pw_list.txt', 'w')

                        #Überschreiben der Zeit mit dem aktuellen Datum und der aktuellen Urzeit 
                        while k < len(text_arr):
                            if text_arr[k] == "Zeit":
                                datei.write("Zeit ")
                                datei.write(str(text_arr[k+1]+" "))
                                datei.write(str(text_arr[k+2]+ " "))
                                k +=2
                            #Alle anderen in der Datei verhandenen informationen werden auch neu geschrieben, da sie sonst gelöscht werden würden
                            else:
                                datei.write(text_arr[k]+" ")
                            k += 1
            j += 1
        datei.close()  