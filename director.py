import Player
import Console
import Roster
import Board

class Director:
    def __init__(self):
        self._roster = Roster()
        self._board = Board()
        self._console = Console()
        self._winnerFound = False

        numPlayers = int(self._console.getInput("How many players?"))
        for i in range(0,numPlayers):
            name = self._console.getPlayerName(i + 1)
            player = Player()
            player.setName(name)
            self._roster.addPlayer(player)

    def startGame():
        while not self._winnerFound:
            for player in self._roster.getPlayers():
                self._console.display(self._board.toString(self._roster.getPlayers()))
                guess = self._console.doTurn(player.getPlayerName())
                player.setLastGuess(guess)
                self._winnerFound = self._board.checkSecretNumber(guess)
                if self._winnerFound:
                    self._console.displayWinner(player.getPlayerName())
                    break