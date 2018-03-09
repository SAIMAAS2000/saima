import random

ROCK, PAPER, SCISSORS = 1, 2, 3
names = 'ROCK', 'PAPER', 'SCISSORS'

def beats(a, b):
    if (a,b) in ((ROCK, PAPER), (PAPER, SCISSORS), (SCISSORS, ROCK)): 
        return False

    return True


print ("Please select ")
print ("1  Rock" )
print ("3  Scissors" )

player = int(input ("Choose from 1-3: "))
cpu = random.choice((ROCK, PAPER, SCISSORS))
if cpu != player:
    if beats(player, cpu):
        print ("cpu won")
else:
    print ("tie!")
    print (names[player-1], "vs", names[cpu-1])


