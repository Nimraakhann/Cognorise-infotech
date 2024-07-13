import random

def xinempty(x) :
 if x in empty :
     print("----Letter Already Guessed----") 
     x = input("Guess a letter ")
  


print("----Welcome To The Hangman Game----")
playagain = "yes"
word_list = [
    "apple", "mountain", "ocean", "sunflower", "giraffe", "eclipse",
    "piano", "castle", "volcano", "rainbow", "orchid", "elephant",
    "galaxy", "chocolate", "tornado", "pyramid", "liberty", "guitar",
    "island", "avocado", "zebra", "savanna", "chameleon", "canyon",
    "sunset", "tulip", "mermaid"
]
while playagain == "yes" :    
  word_selected = random.choice(word_list)
  print(word_selected)
  lst = ["=====","    |","    O","   /|\\","   / \\"]
  for i in lst :
   print(i)
  word_len = len(word_selected)
  word_list.remove(word_selected)
  empty = "_"*word_len
  print(empty)
  print(len(empty), "Letters in the word")
  while lst != [] and empty != word_selected :
   x = input("\n----Guess a letter---- ")
   xinempty(x)
   while x not in word_selected :
    print("\n----Incorrect Guess----")
    lst.pop()
    for i in lst :
     print(i)
    if lst == [] :
     break
    print(empty) 
    x = input("\n----Guess a letter---- ")
    xinempty(x)
   else:
    print("\n----Correct Guess----")
    for i in range(word_len):
      if x == word_selected[i]:
        empty = empty[:i] + x + empty[i+1:]
    for i in lst :
      print(i)
    print(empty)
  else:
    if lst == [] :
      print("\n---------You loose---------")
    elif empty == word_selected :
      print("\n---------You Win---------")    
  playagain = input("\nDo you want to play again? [yes/no]  ")
  while playagain not in ["yes", "no"] :
   playagain = input("\nEnter a valid choice: [yes/no]  ")  
 
