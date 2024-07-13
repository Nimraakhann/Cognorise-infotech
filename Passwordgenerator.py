import random
import string

len = int(input("Enter the length of password: "))
if len < 6 :
  print("Length of Password should be greater than 6")
else:
   characters = string.ascii_letters + string.digits + string.punctuation
   lst = [random.choice(characters) for i in range(len)] 
   password = ''.join(lst)
   print(f"The password generated is : {password}")
