valorProducto = 0
bandera = True

while(bandera):
    print('Listado de productos')
    print('\tA: valor = $270')
    print('\tB: valor = $340')
    print('\tC: valor = $390 \n')
    p = input('Escribe la letra del producto que deseas: ')
    opcion = p.upper()
    if opcion == 'A':
        valorProducto = 270
        bandera = False
    elif opcion == 'B':
        valorProducto = 340
        bandera = False
    elif opcion == 'C':
        valorProducto = 390
        bandera = False
    else:
        print('El producto seleccionado no existe')
        bandera = True
    print('-----------------------------')


print('Solo puedes ingresar monedas de: $10, $50 y $100')
sumaMonedas = 0

while sumaMonedas < valorProducto:
    moneda = int(input('Ingresa una moneda: '))
    if moneda == 10 or moneda == 50 or moneda == 100:
        sumaMonedas += moneda
    else:
        print('Moneda invalida')
        moneda = 0


diferencia = sumaMonedas - valorProducto

if diferencia != 0:
    print('Su vuelto:')

while diferencia != 0:
    if diferencia >= 100:
        vueltos = diferencia - 100
        print(100)
    elif diferencia >= 50 and diferencia < 100:
        vueltos = diferencia - 50
        print(50)
    elif diferencia < 50:
        vueltos = diferencia - 10
        print(10)
    diferencia = vueltos