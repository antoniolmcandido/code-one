def tamanhoLista(lista):
    tamanho = 0
    for i in lista:
        tamanho += 1
    
    return tamanho

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f'Tamanho da lista: {tamanhoLista(lista)}')