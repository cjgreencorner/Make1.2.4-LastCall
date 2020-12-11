#!/usr/bin/env python
"""""""""""""""""""""

"""""""""""""""""""""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory
import platform

# CONFIGURATIONS
# IP = PiGPIOFactory(host='192.168.0.210')

def main():
    print("=" * 40, "System Information", "=" * 40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    
    
if __name__ == '__main__':
    main()
