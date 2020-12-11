import socket
from datetime import datetime



st1 = ""
en1 = ""
net2 = ""
def scan(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr, 135))
    if result == 0:
        return 1
    else:
        return 0


def run1():
    global st1
    global en1
    global net2
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        if (scan(addr)):
            print(addr, "leeft")

def main():
    global st1
    global en1
    global net2
    net = input("Voer het IP-Adress in: ")
    net1 = net.split('.')
    a = '.'

    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = int(input("Voer eerste cijfer in: "))
    en1 = int(input("Voer laatste cijfer in: "))
    en1 = en1 + 1
    t1 = datetime.now()


    run1()
    t2 = datetime.now()
    total = t2 - t1
    print("Netwerkscan duur: ", total)

if __name__ == '__main__':
    main()