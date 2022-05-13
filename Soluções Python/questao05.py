pontos = input('Mora perto da vítima? ').lower() == 'sim'
pontos = pontos + (input('Já trabalhouu com a vítima? ').lower() == 'sim')
pontos = pontos + (input('Telefonou para a vítima? ').lower() == 'sim')
pontos = pontos + (input('Esteve no local do crime? ').lower() == 'sim')
pontos = pontos + (input('Devia para a vítima? ').lower() == 'sim')

if pontos == 5:
  print('Você é o assassino!')
elif pontos >= 3:
  print('Cúmplice!')
elif pontos == 2:
  print('Suspeito!')
else:
  print('Liberado')