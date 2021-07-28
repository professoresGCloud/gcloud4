#Questão1
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
  print(f'O maior numero entre {n1} e {n2} é o número {n1}')

if n2 > n1:
  print(f'O maior numero entre {n1} e {n2} é o número {n2}')

if n1 == n2:
  print(f'Os números {n1} e {n2} são iguais')
