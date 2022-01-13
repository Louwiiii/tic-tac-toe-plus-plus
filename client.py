import socket

import main
from game import Game
import pickle
import threading
import _thread


class Client:
    def __init__(self, address):
        ip,port = address

        print("IP:",ip)
        print("Port:",port)

        # TCP based client socket
        s = socket.socket()

        s.connect(address)

        print("Player connected to a game")

        threading.Thread(target=Client.game_loop, args=(self,s)).start()
        main.pygame_loop()

    def game_loop(self,s):
        self.player_number = int(str(s.recv(1024).decode()).split(":",1)[1])
        self.game = Game(0)

        print(f"Player has number {self.player_number}")

        while True:
            # Get the reply
            msg_received = s.recv(1024)
            self.game = pickle.loads(msg_received)
            print("Received the state of the game")
            main.draw_game(self.game)
            if self.game.turn == self.player_number:
                action = "{play}:"+main.get_action()
                s.send(action.encode())
                print("Sent action:")
                print(action)

if __name__ == "__main__":
    print("Please enter the server IP address: ")
    text = input()
    if ":" in text:
        ip, port = text.split(":")
        port = int(port)

    else:
        ip, port = text, 55000
        if ip == "":
            ip = "localhost"
    #finally:
    #    ip, port = "localhost", 55000

    print(f"Trying to connect to {ip}:{port}")
    client = Client((ip, port))

