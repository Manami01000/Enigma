import socket
from Enigma_Machine import *
from threading import Thread

def client_output_handling(client_socket, enigma):
    while True:
        message = enigma.get_phrase(input())
        if message == enigma.get_phrase("bye"):
            client_socket.close()
        else:
            client_socket.send(message.encode())

def client_input_handling(client_socket, enigma):
    while True:
        data = client_socket.recv(1024).decode()
        print(f'Received from server: encrypted {data}, decrypted {enigma.get_phrase(data)}')

def client_program():
    host = socket.gethostname('')  # as both code is running on same pc
    print(host)
    port = 5000  # socket server port number

    enigma = Enigma_Machine('A','I','II','III')
    enigma.multiconnect('asdfghjkl', 'zxcvbnm')
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    input_thread = Thread(target = client_input_handling, args = (client_socket,))
    output_thread = Thread(target = client_output_handling, args = (client_socket, ))
    input_thread.start()
    output_thread.start()
    input_thread.join()
    output_thread.join()

if __name__ == '__main__':
    client_program()
