import socket
import threading




def setup(IP, PORT):
    s = socket.socket()
    print("created")
    s.bind((IP, PORT))
    s.listen()
    print("listening")
    p, adr = s.accept()

    print("connected with", adr)
    sender = threading.Thread(target=send, args=(p,))
    sender.start()
    while True:



        r = p.recv(1024).decode()
        print("received:", r)



    return s
def send(port):
    while True:
        m = input("\n")
        port.send(bytes(m ,'ascii'))



#architecture sgbd


