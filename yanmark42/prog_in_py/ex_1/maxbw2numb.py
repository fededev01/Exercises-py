# Given two numbers the program prints the greater
# Implemented errors to be sure the user only inputs a number and not a letter or a symbol

print('Input 2 numbers\n')

while True:
    try:
        a = int(input('The first: '))
        break
    except ValueError: print("Just numbers!")

while True:
    try:
        b = int(input('The second: '))
        break
    except ValueError: print("Just numbers!")

if (a > b): 
    print(a, 'is the highest number')
    
elif (a < b):
    print (b, 'is the highest number')  
    
else:
    print ('The numbers are equal') 
