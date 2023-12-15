def calcularAlzaMayor(valorDolar):
    alzaMayor = 0
    contador = 0
    for i  in valorDolar:
        if contador != 0:
            if valorDolar[contador] - valorDolar[contador - 1] > alzaMayor:
                alzaMayor = valorDolar[contador] - valorDolar[contador - 1]
        contador += 1
    return alzaMayor


dia = int(input('numero de dias: '))
valorDolar = []

for i in range(0, dia):
    valorDia = float(input(f'dia {i}: '))
    valorDolar.append(valorDia)

print(calcularAlzaMayor(valorDolar))