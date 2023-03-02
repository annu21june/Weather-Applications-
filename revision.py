def divide_integers():
    
try:

  a = int(input("Enter a:"))

  b = int(input("Enter b:"))

  c = a/b

  print("a/b = %d"%c)

# Using exception object with the except statement

except ZeroDivisionError as e:

  print("can't divide by zero")

  print(e)

  print(type(e))

else:

 print("Hi I am else block")