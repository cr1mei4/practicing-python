print('DIVISÃO PLUS\n'
      '------------')

dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))

quo = dividendo / divisor
quo2 = dividendo // divisor
resto = dividendo % divisor

print(f'\nDivisão normal: {quo:.2f}')
print(f'Divisão inteira: {quo2}')
print(f'Resto: {resto}')
