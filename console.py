
class Console:

    def getInput(self, message):
        return input(message)

    def display(self, message):
        print(message)

    def getPlayerName(self, player):
        return(input(f"Enter a name for player {player}"))
    
    def doTurn(self, name):
        x = 0
        invalid = true
        while invalid
            print(f"{name}'s turn: ")
            x = (int(input("What is your guess? ")))
                if x >=1000 and <= 9999:
                    invalid = false
                else:
                    print("Incorrect. Choose a number between 1000 and 9999")
        return x
    def displayWinner(self, name):
        print(f"{name} won!")
    
    
        
