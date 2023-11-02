#!python3
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""
import random
def computerChoice():
  compChoice=random.randint(0, 2)
  print('Computer chooses: ',end="")
  if compChoice==0:
    print('rock')
  elif compChoice==1:
    print('paper')
  else:
    print('scissors')
  return compChoice


if __name__ == "__main__":
  pass