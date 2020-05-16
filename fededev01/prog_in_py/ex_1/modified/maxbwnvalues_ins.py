lista = []

fine_inserimento = False
while not fine_inserimento:
  inserimento = input("enter your number or stop with 'x': \n")
  if inserimento == 'x':
      fine_inserimento = True
  else:
       num = int(inserimento)
       lista.append(num)

print(lista)

def max_in_list(x):
    max = 0
    for numero in range(len(x)):
        if x[numero] > max:
            max = x[numero]
    print('Il numero più grande della lista è ' + str(max))


max_in_list(lista)