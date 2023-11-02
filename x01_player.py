#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  PlayChoice = input('Rock, Paper, Scissors:')
  PlayChoice=PlayChoice.lower()
  PlayChoice=PlayChoice.replace(' ','')
  print('Player chooses:',PlayChoice)
  if PlayChoice=='rock':
    PlayChoice=0
  elif PlayChoice=='paper':
    PlayChoice=1
  elif PlayChoice=='scissors':
    PlayChoice=2
  else:
    PlayChoice=None
  return PlayChoice


if __name__ == "__main__":
  pass