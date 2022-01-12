import socket
from game import Game
import _thread
import threading
import pickle

class Server:
    def __init__(self, port):
        self.games = {}
        self.clients = {}

        games_id_count = 0
        clients_id_count = 0

        # TCP based server
        self.server_socket = socket.socket()
        self.address = (socket.gethostname(), port)

        # Bind the socket to the public host and the given port
        try:
            self.server_socket.bind(self.address)
        except socket.error as e:
            str(e)

        # Listen for incoming connections
        self.server_socket.listen()

        print("Server started")
        while True:
            client = self.server_socket.accept()
            client_id = clients_id_count

            self.clients[client_id] = client

            clients_id_count += 1

            game_id = games_id_count

            if len(self.clients)%2 == 1:
                # Start a new game
                player_number = 0
                self.games[game_id] = Game(game_id)
            else:
                # Add client to the last game
                player_number = 1
                games_id_count += 1

            self.games[game_id].players_ids.append(client_id)

            #_thread.start_new_thread(client, game_id)
            threading.Thread(target=self.threaded_client, args=(client, game_id, player_number)).start()


    def threaded_client (self, client, game_id, player_number):
        client_socket, client_address = client

        client_socket.send("{player_number}:"+str(player_number).encode())

        # Handle one request from client
        try:
            while True:
                data = client_socket.recv(1024)

                print("Received data:\n", data)

                if (data != b''):
                    tag, content = data.decode().split(":",1)
                    if tag == "{play}":
                        self.games[game_id].play(player_number, content)

                    opponent_id = self.games[game_id].players_ids[(player_number + 1) % 1]
                    opponent_socket, opponent_address = self.clients[opponent_id]
                    opponent_socket.send(pickle.dumps(self.games[game_id]))
        except:
            print(f"Connection with client {client_address} was lost")

        try:
            del self.games[game_id]
            print(f"Game number {game_id} closed")
        except:
            print(f"Could not delete game number {game_id}")

        client_socket.close()


if __name__ == "__main__":
    print("You are starting a new server, please enter the port the server should run on:")
    try:
        port = int(input())
        print("Server started on port", port)
    except:
        port = 5500
        print("Port was incorrect, server started on port", port)

    server = Server(port)