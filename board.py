import random
from player import Player

class Board:
    def __init__(self):
        self._secretNumber = random.randrange(1000, 10000)
        print(self._secretNumber)
    
    def _getHintString(self, guess):
        if (guess < 1000 or guess > 9999):
            return "****"
        hintString = ""
        strGuess = str(guess)
        strSecret = str(self._secretNumber)
        for i in range(len(strGuess)):
            if strGuess[i] == strSecret[i]:
                hintString += 'x'
            elif strGuess[i] in strSecret:
                hintString += 'o'
            else:
                hintString += '*'
        return hintString

    def toString(self, players):
        boardString = "--------------------\n"
        for player in players:
            boardString += f"Player {player.getName()}: {str(player.getLastGuess())}, {self._getHintString(player.getLastGuess())}\n"
        boardString += "--------------------\n"
        return boardString
        
    def checkSecretNumber(self, number):
        return True if number == self._secretNumber else False