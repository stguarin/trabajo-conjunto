##Descuento en una respectiva factura
## Autores Arnold Joseph Merchan Rojas  y Santiago Guarin Alfaro
# primero mostramos el menu en pantalla
print('Menu\n1:     Haburguesa      $10.000\n2:     Papas fritas    $6.000\n3:     Bebida          $4.000')
# predefinimos variables para usar posteriormente, y evitar problemas en el codigo mas adelante
orden = 1
costo_H = 0
costo_P = 0 
costo_B = 0
cantida_H=0
cantidad_b=0
cantida_p=0
#cree un bucle para solicitar la orden, si prefieres lo puedo dejar para que pida la orden de forma completa en lugar de usar el bucle
while orden != 0:
    orden = int(input('dijite el indice de la comida que desea solicitar, si desea finalizar su orden dijite el numero 0 '))
    #confirmo si el valor del indice coincide con los del menu
    if orden >= 0 and orden <= 3:
        ##se pide la cantidad de cada producto y su repectivo costo
        if orden == 1:
            hamburguesas = int(input('ingrese la cantidad de hamburguesas de desea comprar '))
            cantida_H = cantida_H + hamburguesas
            costo_H =cantida_H * 10000
        elif orden == 2:
            papas_fritas = int(input('ingrese la cantidad de papas fritas que desa comprar '))
            cantida_p = cantida_p + papas_fritas
            costo_P = cantida_p * 6000
        elif orden == 3:
            bebidas = int(input('ingrese la cantiadad de bebidas que desea comprar '))
            cantidad_b = cantidad_b + bebidas
            costo_B = cantidad_b * 4000
        else:
            print('oreden finalizada')
    else:
        print('por favor dijite un indice valido para la orden')
        #confirmacion para romper el bucle
total = costo_H+costo_B+costo_P
#impresion de una factura prelliminar sin descuentos 
print(f'el valor total de la factura sin descuento es de \n{hamburguesas}  Haburguesa      ${costo_H}\n{papas_fritas}  Papas fritas    ${costo_P}\n{bebidas}  Bebida          ${costo_B}\nTotal sin descuento:    ${total}')
## encontrar el descuento de cada producto y el valor total de la factura
if(cantida_H>=20):
    costo_H = costo_H-(costo_H * 20)/100
    print(f'el valor de sus hamburguesas con descuento del 20% es de\n Hamburguesas    ${costo_H}')
elif(cantida_H >=10):
    costo_H = costo_H-(costo_H * 10)/100
    print(f'el valor de sus hamburguesas con descuento del 10% es de\n Hamburguesas    ${costo_H}')
elif(cantida_H >=5):
    costo_H = costo_H-(costo_H * 5)/100
    print(f'el valor de sus hamburguesas con descuento del 5% es de\n Hamburguesas    ${costo_H}')


if(cantida_p>=20):
    costo_P = costo_P-(costo_P * 20)/100
    print(f'el valor de sus papas fritas con descuento  del 20% es de\n Papas Fritas    ${costo_P}')
elif(cantida_p >=10):
    costo_P = costo_P-(costo_P * 10)/100
    print(f'el valor de sus papas fritas con descuento  del 10% es de\n Papas Fritas    ${costo_P}')
elif(cantida_p >=5):
    costo_P = costo_P-(costo_P * 5)/100
    print(f'el valor de sus papas fritas con descuento  del 5% es de\n Papas Fritas    ${costo_P}')




if(cantidad_b>=20):
    costo_B = costo_B-(costo_B * 20)/100
    print(f'el valor de su Bebida con descuento  del 20% es de\n Bebida    ${costo_B}')
elif(cantidad_b >=10):
    costo_B = costo_B-(costo_B * 10)/100
    print(f'el valor de su Bebida con descuento  del 10% es de\n Bebida    ${costo_B}')
elif(cantidad_b >=5):
    costo_B = costo_B-(costo_B * 5)/100
    print(f'el valor de su Bebida con descuento  del 5% es de\n Bebida    ${costo_B}')

total_des = costo_H+costo_B+costo_P
print(f'el valor total de la factura con descuento es de \n{hamburguesas}  Haburguesa      ${costo_H}\n{papas_fritas}  Papas fritas    ${costo_P}\n{bebidas}  Bebida          ${costo_B}')
print(f'el valor total de la facturaa con descuento es de: ${total_des}')