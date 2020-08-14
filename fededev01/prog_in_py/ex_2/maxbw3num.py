fir = int(input("Insert your first number\n"))

sec = int(input("Insert your second number\n"))

thir = int(input("Insert your third number\n"))

if fir > sec and fir > thir:
    print("The greather number is:\n")
    print(fir)
elif sec > fir and sec > thir:
    print("The greather number is:\n")
    print(sec)
elif thir > fir and thir > sec:
    print("The greather number is:\n")
    print(thir)    
elif thir == fir == sec:
    print("Your numbers are identical")
else: 
    print("Unknown input")        