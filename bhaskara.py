resp = ''

while resp != 'sair':
    print('\nCÁLCULO DE BHASKARA\n'
          '-------------------')
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('\nNão possui raiz real!')
        resp = input("\nDeseja continuar calculando('sair' para sair)?")
    elif delta == 0:
        raiz1 = (-b + delta ** 0.5) / (2 * a)
        print('\nPossui apenas uma raiz real!\n')
        print(f'Raiz: {raiz1}')
        resp = input("\nDeseja continuar calculando('sair' para sair)?")
    else:
        raiz1 = (-b + delta ** 0.5) / (2 * a)
        raiz2 = (-b - delta ** 0.5) / (2 * a)
        print(f'\nO valor de delta é: {delta}\n')
        print(f'O valor da raiz 1 é: {raiz1}')
        print(f'O valor da raiz 2 é: {raiz2}')
        resp = input("\nDeseja continuar calculando('sair' para sair)?")

print('\n' + '-' * 10 + 'Fim do programa' + '-' * 10)


