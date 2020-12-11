#!/usr/bin/env python
"""""""""""""""""""""

"""""""""""""""""""""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory
import Wachtwoord, Rekenmachine, Netwerk
import subprocess

# CONFIGURATIONS
# IP = PiGPIOFactory(host='joel')


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"


# FUNCTIONS
def main():
    print("1 = Rekenmachine")
    print("2 = Random wachtwoord generator")
    print("3 = Update RPi")
    print("4 = IP-Adress RPi")
    print("5 = RPi Systeem Info")
    print("6 = Verander Netwerkinstellingen")
    print("7 = Netwerkscanner")
    print("8 = GPIO-Pins RPi")
    print("9 = Installeer volledige LAMP-stack")


    keuze = int(input("Maak uw keuze: "))
    if keuze == 1:
        Rekenmachine.main()
        main()
    if keuze == 2:
        Wachtwoord.main()
        main()
    if keuze == 3:
        subprocess.Popen('update.ps1')
        main()
    if keuze == 4:
        subprocess.Popen('ipadress.ps1')
        main()
    if keuze == 5:
        subprocess.Popen('systeminfo.ps1')
        main()
    if keuze == 6:
        subprocess.Popen('wifi.ps1')
        main()
    if keuze == 7:
        Netwerk.main()
        main()
    if keuze == 8:
        subprocess.Popen('pinout.ps1')
        main()
    if keuze == 9:
        subprocess.Popen('lamp.ps1')
        main()

if __name__ == '__main__':
    main()
