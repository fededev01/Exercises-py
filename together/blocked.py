def max_in_list(num):
    max = 0

num = []

sed = input("Do you want add a number?\n")

if sed == si:
    num.append((int(input("enter your first number\n"))))
else: print ("ok")    





x = num.copy()
print("Your numbers are: " + x)

for numero in num:
        if numero > max:
            max = numero
print('Il numero più grande della lista passata è ' + str(max))


max_in_list(num)
