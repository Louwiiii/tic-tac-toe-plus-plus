import socket
from game import Game
import pickle


class Client:
    def __init__(self, address):
        ip,port = address

        print("IP:",ip)
        print("Port:",port)

        # TCP based client socket
        s = socket.socket()

        s.connect(address)

        print("Player connected to a game")

        self.player_number = s.recv(1024).decode()
        self.game = Game(0)

        print(f"Player has number {self.player.number}")

        while True:
            message = input()

            # Send a message
            s.send(message.encode())

            # Get the reply
            msgReceived = s.recv(1024)

            self.game = pickle.loads(msgReceived)

            # Print the reply
            print("Received :\n"+msgReceived.decode())


if __name__ == "__main__":
    try:
        text = input("Please enter the server IP address: ")
        if ":" in text:
            ip, port = text.split(":")
            port = int(port)

        else:
            ip, port = text, 5500
            if ip == "":
                ip = "localhost"
    except:
        ip, port = "localhost", 5500

    print(f"Trying to connect to {ip}:{port}")
    client = Client((ip, port))
