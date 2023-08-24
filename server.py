from threading import Thread
import socket

def server_input_handling(conn, conns):
    while True:
        data = conn.recv(1024).decode()
        for i in conns:
            i.send(data.encode())


def connection_handling(socket,conns = []):
    while True:
        conn, address = socket.accept()
        conns.append(conn)
        print(str(address) + " connected")
        input_thread = Thread(target = server_input_handling, args = (conn, conns))
        input_thread.start()
#rememeber to socket close

def server_program():
    # get the hostname
    host = ""
    print("host: " + host)
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind(("", port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print("server ready")
    conns = []
    conn_thread = Thread(target = connection_handling, args = (server_socket, conns))
    conn_thread.start()
    conn_thread.join()

if __name__ == '__main__':
    server_program()