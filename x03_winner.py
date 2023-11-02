#!python3

'''
Create a function that takes 2 input parameters:
int: computer choice
int: player choice

the choices correspond to:
0: rock
1: paper
2: scissors

Based on the classic rules for Rock Paper Scissors, the return value should be an integer value that indicates if the player is the wins, loses or ties
Output:
-1: player loses
0: tie
1: player wins
'''

#from x01_player import playerChoice
#from x02_computer import computerChoice

#player=playerChoice()
#computer = computerChoice()

def playerWins(computer,player):
  if player==computer:
    gameOutcome=0
  elif player==(computer+1)%3:
    gameOutcome=1
  else:
    gameOutcome=-1
  print(gameOutcome)
  return gameOutcome

if __name__ == "__main__":
  assert playerWins(1,1) == 0
  assert playerWins(1,0) == -1
  assert playerWins(1,2) == 1
  assert playerWins(2,1) == -1
  
