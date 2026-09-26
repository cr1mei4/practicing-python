print('DIVISÃO PLUS\n'
      '------------')

dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))

if divisor == 0:
    print('O divisor não pode ser 0.')
    dividendo = int(input('Digite o dividendo: '))
    divisor = int(input('Digite o divisor: '))

quo = dividendo / divisor
quo2 = dividendo // divisor
resto = dividendo % divisor

print(f'\nDivisão normal: {quo:.2f}')
print(f'Divisão inteira: {quo2}')
print(f'Resto: {resto}')
