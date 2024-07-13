import random
import string

len = int(input("Enter the length of password: "))
while len < 6 :
  
  len = int(input("Length of Password should be greater than 6: "))
else:
   characters = string.ascii_letters + string.digits + string.punctuation
   lst = [random.choice(characters) for i in range(len)] 
   password = ''.join(lst)
   print(f"The password generated is : {password}")
