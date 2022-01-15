# tic-tac-toe-plus-plus

Tic-tac-toe++ is an improved version of the Tic-Tac-Toe game.

This project contains a script for servers and clients in order to host and play multiplayer games.

Rules of the game :

The game plays on a 9x9 grid containing 9 grid of the original Tic-tac-toe game.
When winning on a small grid, this entire grid will be replaced by the symbol of the winning player.
To win the game, you have to align three symbols on the big grid.


How to play :

To host games, start a server by running the server.py script with python. Choose the port the server will be running on. You may need to forward connections to this port to your server in your router settings.

To connect to a server, run the client.py script and enter the ip and port of the server you want to connect to (ip:port).
