
class Player:
    def __init__(self, name):
        self._name = name
        self._lastGuess = 0
        
    def getPlayerName(self):
        return self._name
    
    def setPlayerName(self, name):
        self._name = name

    def getLastGuess(self):
        return self._lastGuess
        
    def setLastGuess(self, guess):
        self._lastGuess = guess

    
        
