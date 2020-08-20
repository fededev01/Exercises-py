x = [20,30,10]

if x[0] == x[1] == x[2]:
    print("Your numbers are identical")
elif x[0] > x[1] and x[0] > x[2]:
    print("The greather number is:\n")
    print(x[0])   
elif x[0] < x[1] and x[1] > x[2]:
    print("The greather number is:\n")
    print(x[1])
elif x[2] > x[1] and x[0] < x[2]:
    print("The greather number is:\n")
    print(x[2])   
else: 
    print("Unknown input")     