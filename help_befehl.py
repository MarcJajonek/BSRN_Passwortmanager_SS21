#!/usr/bin/env python3

def fixed_lenght(text, lenght):
        if len(text) > lenght:
            text = text[:lenght]
        elif len(text) < lenght:
            text = (text + " " * lenght)[:lenght]
        return text

def help_Befehl():
    print("List of all Funtions:\n"
            +fixed_lenght("--> add:", 15)+"-title *yourtitle* -username *yourusername* -password *yourpassword*\n"
            "                Or --> you can also generate a password with -genratepw\n \n"
            +fixed_lenght("--> change:", 15)+"-title *title for the password you want to change* -password *newpassword*\n"
            "                Or --> you can also generate a new password with  -generatepw\n \n"
            +fixed_lenght("--> delete:", 15)+"-title *title you want to delete* \n \n"
            +fixed_lenght("--> copy:", 15)+"-title *title for the password you want to copy* \n \n"
            +fixed_lenght("--> changemp:", 15)+"-password *new master-password*\n \n"
            +fixed_lenght("--> table:", 15)+"shows all titles and the matching usernames for the passwords you saved \n")
