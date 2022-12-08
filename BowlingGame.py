#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls=[] # list called rolls is created

    def roll(self,pins):
        self.rolls.append(pins) # this function adds to roll list

    def score(self):  # this method (calling it method cause thats what criteria says) scores the game
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if frameIndex in range(10):
                result += self.StrikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
            rollIndex +=2
            return result

    def isStrike(self, rollIndex):  # if index position equals 10 strikes, return value for stike = 10
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):   # if 2 index position equals 10, then it is a spare. 
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10 # this line counts the 2 pins to determine if it is a spare
    
    def stickeScore(self,rollIndex): # if index position is 10, it is a strike
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2] # scoring a strike

    def spareScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		