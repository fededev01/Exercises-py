mylist =[]
for x in range(2):
 inp = int(input("Inserisci un numero\n"))
 mylist.append(inp)
print("I numeri da te scelti sono:") 
print(mylist)
if mylist[0] > mylist[1]:
 print("Il primo numero è il più grande\n")
elif mylist[0] == mylist[1]:
 print("I due numeri sono uguali\n")
else:
 print("Il secondo numero è il più grande ")