#!/usr/bin/env python
"""""""""""""""""""""

"""""""""""""""""""""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory
import Wachtwoord, Rekenmachine
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


if __name__ == '__main__':
    main()
