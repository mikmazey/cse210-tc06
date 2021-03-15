from player import Player

class Roster:

    def __init__(self):
        self._players = []
    
    def addPlayer(self, player):
    #adding the player to the list above
        self._players.append(player)

    def getPlayers(self): 
        return self._players

    def getNumPlayers(self, player):
        return len(self._players)
