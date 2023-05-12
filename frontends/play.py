from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import Player, RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.players import ConsolePlayer
from console.renders import ConsoleRenderer

# player1 = RandomComputerPlayer(Mark("X"))
player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()
