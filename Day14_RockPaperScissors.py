from getpass import getpass as input

print("    EPIC BATTLE") 
print("ROCK PAPER SCISSORS")
print()
print("Enter your move: (R,P,S)")
p1 = input("Player1: ")
p2 = input("player2: ")

if p1 == p2:
  print("Move Cancelled!")
elif p1 == 'R' and p2 == 'S':
  print("Player 1 wins!")
elif p2== 'R' and p1== 'S':
  print("Player 2 wins!")
elif p1 == 'P' and p2 == 'R':
  print("Player 1 wins!")
elif p2== 'P' and p1== 'R':
  print("Player 2 wins!")
elif p1 == 'S' and p2 == 'P':
  print("Player 1 wins!")
elif p2== 'S' and p1== 'P':
  print("Player 2 wins!")
else:
  print("You Put the wrong hand!")
