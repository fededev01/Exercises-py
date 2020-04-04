lista = []
lista.append((int(input("enter your new number\n"))))
lista.append((int(input("enter your new number\n"))))
lista.append((int(input("enter your new number\n"))))
lista.append((int(input("enter your new number\n"))))


x = lista.copy()
print("Your numbers are: ") 
print(x)

def max_in_list(lista):
    max = 0
    for numero in lista:
        if numero > max:
            max = numero
    print('Il numero più grande della lista passata è ' + str(max))


max_in_list(lista)

