import socket



def server():
    PORT = 64111

    #creates a welcoming socket-
    with socket.socket() as myserversocket:
        myserversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        myserversocket.bind(("127.0.0.1",PORT))
        myserversocket.listen()
        print("Server listening....")

        while True:
            connectionSocket,address = myserversocket.accept()
            client_address = connectionSocket.getpeername()
            print(f"Connection Established with {client_address}")
            print("Waiting for message...")
            print("Type /q to quit")
            while True:
                incoming_message = connectionSocket.recv(4096).decode()
                # if close message from client
                if incoming_message == "/q":
                    print("Connection Terminated")
                    break
                elif incoming_message == "play game":
                    #connectionSocket.send(incoming_message.encode())
                    game(connectionSocket)
                else:
                    print(incoming_message)
                return_message = input("Enter a message: ")
                # if server wants to close connection
                if return_message == "/q":
                    connectionSocket.send(return_message.encode())
                    print("Connection terminated")
                    break
                elif return_message == "play game":
                    connectionSocket.send(return_message.encode())
                    game(connectionSocket)
                else:
                    connectionSocket.send(return_message.encode())
            connectionSocket.close()
            break
        myserversocket.close()


def game(socket):
    print("Welcome to rock paper scissors! Wait for your opponents turn")
    incoming_message = socket.recv(4096).decode()
    print(incoming_message)
    server_move = input("Enter your move, pick between rock paper or scissors: ")
    socket.send(server_move.encode())





def main():
    server()


if __name__ == "__main__":
    main()