lista = list(map(int, input('Informe os numeros da lista: ').split(' ')))
soma = 0

for i in lista:
  soma += i

print('Soma dos elementos da lista =', soma)