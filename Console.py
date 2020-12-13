#!/usr/bin/env python
"""""""""""""""""""""
This Python script is multifunctional and has multiple scripts imported.
"""""""""""""""""""""
# IMPORTS
import Rekenmachine, Wachtwoord, subprocess, Systeminfo, Netwerk # Imports from other scripts and also subprocess


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


# FUNCTIONS
def main():
    print("1 = Calculator") # Some text for the user
    print("2 = Random password generator")
    print("3 = Update RPi")
    print("4 = IP-Adress RPi")
    print("5 = System Info")
    print("6 = Change Network Settings")
    print("7 = Networkscanner")
    print("8 = GPIO-Pins RPi")
    print("9 = Install full LAMP-stack")


    choice = int(input("Make a choice: ")) # Ask the user for a number
    if choice == 1: # This happens if the user chose the first function
        Rekenmachine.main() # Import the main function of the script
        main() # After after running the main function of the 'Rekenmachine' function, restart the program
    if choice == 2:
        Wachtwoord.main()
        main()
    if choice == 3:
        subprocess.check_output(["./update"]) # Execute a bash file
        main()
    if choice == 4:
        subprocess.check_output(["ifconfig"]) # Show IP-Adress of the RPi
        main()
    if choice == 5:
        Systeminfo.main()
        main()
    if choice == 6:
        subprocess.call("./wifi")
        main()
    if choice == 7:
        Netwerk.main()
        main()
    if choice == 8:
        subprocess.check_output(["gpio", "readall"])
        main()
    if choice == 9:
        subprocess.call("./lamp")
        main()

if __name__ == '__main__':
    main()
