lista = []

how_many = int(input("Quanti numeri vuoi inserire? \n"))


for x in range(how_many):
    num = int(input("Insert here your number: \n"))
    lista.append(num)
    
    
'''
il metodo .copy() serve per copiare una lista
'''
# m = lista.copy()
print("Your numbers are: ") 
print(lista)

def max_in_list(list):
    max = 0
    for numero in lista:
        if numero > max:
            max = numero
    print('Il numero più grande della lista è ' + str(max))


max_in_list(lista)
