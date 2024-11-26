# primero mostramos el menu en pantalla
print('Menu\n1:     Haburguesa      $10.000\n2:     Papas fritas    $6.000\n3:     Bebida          $4.000')
# predefinimos variables para usar posteriormente, y evitar problemas en el codigo mas adelante
terminar = 'no'
costo_H = 0
costo_P = 0 
costo_B = 0
#cree un bucle para solicitar la orden, si prefieres lo puedo dejar para que pida la orden de forma completa en lugar de usar el bucle
while terminar != 'si':
    orden = int(input('dijite el indice de la comida que desea solicitar '))
    #confirmo si el valor del indice coincide con los del menu
    if orden >= 1 and orden <= 3:
        if orden == 1:
            hamburguesas = int(input('ingrese la cantidad de hamburguesas de desea comprar '))
            costo_H =hamburguesas * 10000
        elif orden == 2:
            papas_fritas = int(input('ingrese la cantidad de papas fritas que desa comprar '))
            costo_P = papas_fritas * 6000
        else:
            bebidas = int(input('ingrese la cantiadad de bebidas que desea comprar '))
            costo_B = bebidas * 4000
    else:
        print('por favor dijite un indice valido para la orden')
        #confirmacion para romper el bucle
    terminar = input('desea finalizar la orden ? si/no ')
total = costo_H+costo_B+costo_P
#impresion de una factura prelliminar sin descuentos 
print(f'el valor total de la factura sin descuento es de \nHaburguesa      ${costo_H}\nPapas fritas    ${costo_P}\nBebida          ${costo_B}')