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
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ("", port)
        print(self.address)

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

            print(f"Client number {client_id} connected")

            self.clients[client_id] = client

            clients_id_count += 1

            available_game = None
            for game in self.games.values():
                if len(game.players_ids) == 1:
                    available_game = game.id
                    break

            if available_game is None:
                # Start a new game
                game_id = games_id_count
                player_number = 0
                self.games[game_id] = Game(game_id)
                print(f"Created game number {game_id}")
                games_id_count += 1
            else:
                # Add client to the last game
                game_id = available_game
                player_number = 1
                print(f"Game number {game_id} started")

            self.games[game_id].players_ids.append(client_id)

            threading.Thread(target=self.threaded_client, args=(client, game_id, player_number)).start()


    def threaded_client (self, client, game_id, player_number):
        client_socket, client_address = client

        client_socket.send(("{player_number}:"+str(player_number)).encode())

        if player_number == 1:
            first_player_socket, first_player_address = self.clients[self.games[game_id].players_ids[0]]
            # Send the board to the first player so that he can start to play
            print("Board has been sent to player 0 and game has started")
            first_player_socket.send(pickle.dumps(self.games[game_id]))

        # Handle one request from client
        try:
            while True:
                data = client_socket.recv(1024)

                if (data != b''):
                    print("Received data:\n", data)
                    tag, content = data.decode().split(":",1)
                    if tag == "{play}":
                        print(f"Player number {player_number} played")
                        action_is_valid = self.games[game_id].play(player_number, content)
                        print(f"Action valid:",action_is_valid)

                    opponent_id = self.games[game_id].players_ids[(player_number + 1) % 2]
                    opponent_socket, opponent_address = self.clients[opponent_id]
                    client_socket.send(pickle.dumps(self.games[game_id]))
                    print("Sent game to player")
                    opponent_socket.send(pickle.dumps(self.games[game_id]))
                    print("Sent game to opponent")
        except Exception as e:
            print(e)
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
        port = 55000
        print("Port was incorrect, server started on port", port)

    server = Server(port)