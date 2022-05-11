n = 5
while True:
  try: print("%s divisível por %d." %("É" if int(input("Informe o número: ")) % n == 0 else "Não é", n))
  except ValueError: print('Número não informado ou palavra.'); break