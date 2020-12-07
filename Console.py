#!/usr/bin/env python
"""""""""""""""""""""

"""""""""""""""""""""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory
import Wachtwoord
import Rekenmachine
import os

# CONFIGURATIONS
# IP = PiGPIOFactory(host='joel')


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"


# FUNCTIONS
def main():
    print("1 = Rekenmachine")
    keuze = int(input("Maak uw keuze: "))
    if keuze == 1:
        Rekenmachine.main()
        os.system('cls')
        main()
    if keuze == 2:
        Wachtwoord.main()


if __name__ == '__main__':
    main()
