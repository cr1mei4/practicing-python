print('CALCULO DE RAIZ\n'
      '---------------')

num = int(input('Digite o número a ser calculado a raiz: '))
while num < 0:
      print('A raiz de um número negativo não existe no conjunto dos número reais!\n')
      print('CALCULO DE RAIZ\n'
            '---------------')
      num = int(input('Digite o número a ser calculado a raiz: '))

raiz = num ** (1/2)

print(f'\nA raiz de {num} é: {raiz:.2f}')