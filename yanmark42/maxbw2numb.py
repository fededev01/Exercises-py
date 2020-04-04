#Given two numbers the program prints the highest and checks wether the input is a number or not

i=1

while i==1:
    print('Input 2 numbers\n')

    a = input('The first: ')

    if a.isalpha(): 
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
