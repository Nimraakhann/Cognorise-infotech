import random

playagain = "yes"
uc_score = 0
cc_score = 0
print("----Welcome To The Rock Paper Scissors Game----")

while playagain == "yes" :
 uc = input("\nEnter your choice: [rock, paper, scissors]  ")
 while uc not in ["rock", "paper", "scissors"] :
   uc = input("Enter a valid choice: [rock, paper, scissors]  ")
 else:
  print("You chose:", uc)
  print("Computer is thinking...")
  cc = random.choice(["rock", "paper", "scissors"])
  print("Computer chose:", cc)
  if uc == cc :
    print("It's a tie!")
  elif (uc == "rock" and cc == "scissors") or (uc == "paper" and cc == "rock")  or (uc == "scissors" and cc == "paper") :
    print("You win!")
    uc_score += 1
  else :
    print("You lose!")
    cc_score += 1
  playagain = input("Do you want to play again? [yes/no]  ")
  while playagain not in ["yes", "no"] :
   playagain = input("Enter a valid choice: [yes/no]  ")
else:
   print("Your score:", uc_score)
   print("Computer's score:", cc_score)
