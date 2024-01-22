import socket

def client():
    HOST = "127.0.0.1"
    PORT = 64111

    with socket.socket() as mysocket:
        mysocket.connect((HOST, PORT))
        print("Connected to localhost on Port 64111")
        print("Type /q to quit")
        print("Enter a message to send when prompted")
        print("You can type 'play game' to start a game of rock paper scissors")
        while True:
            client_message = input("Enter a message>")
            # if client is sending close message
            if client_message == "/q":
                mysocket.send(client_message.encode())
                print("Connection terminated")
                break
            elif client_message == "play game":
                mysocket.send(client_message.encode())
                game(mysocket)
            else:
                mysocket.send(client_message.encode())
            # receiving message
            message = mysocket.recv(4096).decode()
            # if server sent a close message
            if message == "/q":
                print("Connection terminated")
                break
            elif message == "play game":
                game(mysocket)
            else:
                print(message)
        mysocket.close()


def game(socket):
    print("Welcome to rock paper scissors! Please select between rock paper or scissors: ")
    client_play = input("Enter your play: ")
    if client_play == "rock" or "paper" or "scissors":
        message = "Your opponent has chosen"
        socket.send(message.encode())
        server_play = socket.recv(4096).decode()
        if server_play == "rock" or "paper" or "scissors":
            print(server_play)





def main():
    client()


if __name__ == "__main__":
    main()