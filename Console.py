#!/usr/bin/env python
"""""""""""""""""""""

"""""""""""""""""""""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory
import Wachtwoord, Rekenmachine

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
    keuze = int(input("Maak uw keuze: "))
    if keuze == 1:
        Rekenmachine.main()
        main()
    if keuze == 2:
        Wachtwoord.main()
        main()



if __name__ == '__main__':
    main()
