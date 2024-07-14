import random

sides = int(input("Input the number of sides of the dice: "))
while sides < 2:
    print("The sides should be greater than 1")
    sides = int(input("Input the number of sides of the dice: "))
rolls = int(input("Input the number of rolls: "))

for i in range(rolls):
    print(random.randint(1 , sides))
