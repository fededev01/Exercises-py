num = []
num.append((int(input("enter your first number\n"))))
num.append((int(input("enter your second number\n"))))

if num[0] > num[1]:
    print("The greather number is:\n")
    print(num[0])
elif num[0] == num[1]:
       print("Your numbers are identical")
else:
    print("The greather number is:\n")
    print(num[1])
