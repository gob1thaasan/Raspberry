'''
Use the socket to write a simple web server running on your
Raspberry Pi. When your server receives a request it should print
“Got a request!” to the screen of the Raspberry Pi.

after running this code, use another terminal (installed with netcat) to request for connection, $nc ip_address 55555, for example:

$nc 192.168.0.134 55555
 

Gobithaasan 8/6/2020
'''

import socket

PORT = 55555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', PORT))
    s.listen(5)
    conn, addr = s.accept()
    conn.send(b'Thank you for your request!') #message to requesting client
    with conn:
        print('Got a request!')#message to server
        print('Details:', addr)
        while True:
            data = conn.recv(1000) #string from client is saved as data
            conn.send(b'Ctl-C to exit\n')#message to client
            if not data:
                break
            conn.send(b'You entered: ')# client echo
            conn.sendall(data) # client's string
    conn.close()
    s.close()


