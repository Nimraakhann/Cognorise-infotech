import random

def inguessed(x, guessed) :
 if x in guessed :
     print("----Letter Already Guessed ----")
     x = input("\n----Guess a letter---- ") 
 return x


print("----Welcome To The Hangman Game----")
playagain = "yes"
guessed = []
lst2 = []
word_list = [
    "apple", "mountain", "ocean", "sunflower", "giraffe", "eclipse",
    "piano", "castle", "volcano", "rainbow", "orchid", "elephant",
    "galaxy", "chocolate", "tornado", "pyramid", "liberty", "guitar",
    "island", "avocado", "zebra", "savanna", "chameleon", "canyon",
    "sunset", "tulip", "mermaid"
]
while playagain == "yes" :    
  word_selected = random.choice(word_list)
  
  lst = ["=====","    |","    O","   /|\\","   / \\"]
  for i in lst :
   print(i)
  print("If the hangman is completed like this before you guess the word : YOU LOOSE") 
  word_len = len(word_selected)
  word_list.remove(word_selected)
  empty = "_"*word_len
  print("\nComputer Selecting The Word......")
  print(empty)
  print(len(empty), "Letters in the word")
  while  len(lst2) != 5 and empty != word_selected :
   x = input("\n----Guess a letter---- ")
   x = inguessed(x, guessed) 
   guessed.append(x)
   
   
   while x not in word_selected :
    print("\n----Incorrect Guess----")
    popped = lst.pop(0)
    lst2.append(popped)
    for i in lst2 :
     print(i)
    if len(lst2) == 5 :
     break
    print(empty) 
    x = input("\n----Guess a letter---- ")
    x = inguessed(x, guessed)
    guessed.append(x)
    
   else:
    print("\n----Correct Guess----")
    for i in range(word_len):
      if x == word_selected[i]:
        empty = empty[:i] + x + empty[i+1:]
    for i in lst2 :
      print(i)
    print(empty)
  else:
    if len(lst2) == 5 :
      print("\n---------You loose---------")
      print(f"The word was {word_selected}")
    elif empty == word_selected :
      print("\n---------You Win---------")    
  playagain = input("\nDo you want to play again? [yes/no]  ")
  guessed.clear()
  lst2.clear()
  while playagain not in ["yes", "no"] :
   playagain = input("\nEnter a valid choice: [yes/no]  ")  
 
