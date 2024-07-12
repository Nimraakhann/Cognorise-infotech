a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sign = input("Enter the operation to be performed: ")
if sign == "+" :
  print("the result is: ", a+b)
elif sign == "-" :
  print("the result is: ", a-b)
elif sign == "*" :
  print("the result is: ", a*b)
elif sign == "/" :
  if b == 0 :
    print("Error: Division by zero is not allowed.")
  else :
    print("the result is: ",a/b)
