#Given two numbers the program prints the highest and checks whether the input is a number or not
#doesn't work really well, ignore it, use easier version instead

i=1

while i==1:
    print('Input 2 numbers\n')

    a = input('The first: ')

    if a.isalpha(): #.isalpha checks if the input is a letter
        print('Only numbers!\n')
        continue

    b = input('The second: ')
    if b.isalpha(): 
        print('Only numbers!\n')
        continue

    if (a > b): 
        print(a, 'is the highest number')
        break

    elif (b > a): 
        print (b, 'is the highest number')
        break

    else: 
        print ('The numbers are equal')
        break
    
i=2
