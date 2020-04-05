print('Enter \"n\" to print the result\n')

def chk(h):
    n = h[0]
    for i in range(len(h)):
        if h[i] > n: n=h[i]
        else: continue
    return n

num=[]
while(True):
    x=input("Enter a number\n")
    if x in ('n'):       
        break
    else:
        x=int(x) #here the code converts the string entered into an integer number
        num.append(x) #then adds the converted number in the list "num"
        continue
print('The greater number in the list',num,' is',chk(num))
