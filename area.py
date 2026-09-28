print('CÁLCULO DE ÁREAS DE FIGURAS\n'
      '---------------------------')

print('1-- Quadrado\n'
      '2-- Triângulo\n'
      '3-- Circulo\n'
      '4-- Sair\n')

opc = int(input("Selecione a figura que deseja calcular a área: "))

while opc != 4:
    if opc == 1:
        lado1 = int(input('Digite o valor do lado 1: '))
        lado2 = int(input('Digite o valor do lado 2: '))
        area_qua = lado1 * lado2
        print(f'\nO valor da área é: {area_qua:.2f}\n')
        opc = int(input("Selecione a figura que deseja calcular a área: "))
    elif opc == 2:
        base = int(input('Digite o valor da base: '))
        altura = int(input('Digite o valor da altura: '))
        area_triang = base * altura / 2
        print(f'\nO valor da área é: {area_triang:.2f}\n')
        opc = int(input("Selecione a figura que deseja calcular a área: "))
    else:
        raio = float(input('Digite o valor do raio: '))
        area_circ = 3.14*(raio**2)
        print(f'\nA área do círculo é: {area_circ:.2f}\n')
        opc = int(input("Selecione a figura que deseja calcular a área: "))

print('\n----------Fim do programa----------')