x = []

def convert(x): 
    return tuple(x)

while True:
   print("Options:")
   print("Enter 'numero' to add two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "numero":
       y = int(input("Enter a number: "))
       x.append(y)
       print(x)
       print(convert(x))
   else:
      print("Unknown input")
