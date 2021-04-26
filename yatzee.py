from random import randint

#0 is the bonus
#1 to 6 is dice rules (number of dice times dice value)

def Game():

    playerPickedRules = [False for i in range(7)]
    gamelength = len(playerPickedRules) - 1

    for t in range(gamelength):
        
        #Throws the dice
        dicerolls = RollDice(6)

        #Possible scores for the first line of rules
        possibleScores = [0]
        for i in range(6):
            possibleScores.append((dicerolls.count(i))*(i)) 
        
        #Greedy Strategy
        (highestValueIndex, highestValue) = Greedy(possibleScores,playerPickedRules)
            
        playerPickedRules[highestValueIndex] = highestValue 

        print(f"{playerPickedRules} {str(possibleScores)} {str(dicerolls)}")

    if sum(playerPickedRules[0:6]) > 62:
        playerPickedRules[0] = 10

    print(f"{playerPickedRules} {str(possibleScores)} {str(dicerolls)}")

def RollDice(n):
    dicerolls = []
    for i in range(n):
        dicerolls.append(randint(1,6))
    return dicerolls

def Greedy(possibleScores, playerPickedRules):
    highestValue = 0
    highestValueIndex = 0
    for i in range(len(possibleScores)):
        if type(playerPickedRules[i]) == bool and possibleScores[i] >= highestValue:
            highestValue = possibleScores[i]
            highestValueIndex = i
    return (highestValueIndex, highestValue)

Game()