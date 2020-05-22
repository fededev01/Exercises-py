print('Enter \"0\" to print the result\n')

def chk(h):
    n = h[0]
    for i in range(len(h)):
        if h[i] > n: n=h[i]
        else: continue
    return n

num=[]
while(True):
    num.append(int(input("Enter a number\n")))
    x=num.pop()
    num.append(x)
    if x==0:
        break
    else:     
        continue
print('The greater number in the list',num,' is',chk(num))
