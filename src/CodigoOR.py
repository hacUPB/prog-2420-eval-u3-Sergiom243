print("Bienvenido a Lavafante")
nombre_usuario = input("Por favor ingrese su nombre: ")

historial_procesos = {}

vehiculo = input('1. Vehiculo convencional/carro \n2.Camioneta\nPor favor indique de que tipo es su vehiculo:')

while vehiculo not in  ['1', '2']:
    print ('Por favor elija una opcion valida entre 1 carro y 2 camioneta')
    vehiculo = input('1. Vehiculo convencional/carro \n2.Camioneta\nPor favor indique de que tipo es su vehiculo: ')

print("Muchas gracias por indicar su tipo de vehiculo, estos son los planes que puede seleccionar para el lavado de su carro")

Plan_1 = []
Plan_2 = []
Plan_3 = []

def registro_lavado():

    Lavado_1 = {
        "Tipo 1" : "Lavado básico",
        "Descripción" : "Es es un lavado exclusivamente de la carroceria del vehiculo con shampoo encerado básico y aclarado",
        "Precio1" : 30000,
        "Precio2" : 38000
    }

    Plan_1.append (Lavado_1)

    Lavado_2 = {
        "Tipo 2" : "Lavado extra",
        "Descripción" : "Lavado externo de carroceria encerado básico y lavado interno de la tapiceria y asientos del vehiculo",
        "Precio1" : 55000,
        "Precio2" : 65000
    }
    
    Plan_2.append (Lavado_2)

    Lavado_3 = {
        "Tipo 3" : "Lavado Premium",
        "Descripción" : "Lavado externo e interno de tapiceria, asientos y aplicación de encerado al vehiculo, lavado de motor, rines, neumáticos",
        "Precio1" : 85000,
        "Precio2" : 95000
    }

    Plan_3.append (Lavado_3)


    for Lavado_1 in Plan_1:
        print(f"Plan#1 \nNombre del plan: {Lavado_1['Tipo 1']}, Descripcion: {Lavado_1['Descripción']}, Precio para Carros: {Lavado_1['Precio1']}, Precio para Camionetas {Lavado_1['Precio2']}")

    for Lavado_2 in Plan_2:
        print(f"Plan#2 \nNombre del plan: {Lavado_2['Tipo 2']}, Descripción: {Lavado_2['Descripción']}, Precio para Carros: {Lavado_2['Precio1']}, Precio para Camionetas: {Lavado_2['Precio2']}")

    for Lavado_3 in Plan_3:
        print(f"Plan#3 \nNombre del plan: {Lavado_3['Tipo 3']}, Descripción: {Lavado_3['Descripción']}, Precio para Carros: {Lavado_3['Precio1']}, Precio para Camionetas: {Lavado_3['Precio2']}")


registro_lavado()


Plan_Seleccionado = input('1. Plan#1\n2. Plan#2\n3. Plan#3\nDespues de revisar los planes y precio según su vehiculo por favor elija el que mas desee:')

while Plan_Seleccionado not in ['1', '2', '3']:
    print('Por favor elija el numero del plan que desee correctamente')
    Plan_Seleccionado = input('1. Plan#1\n2. Plan#2\n3. Plan#3\nDespues de revisar los planes y precio según su vehiculo por favor elija el que mas desee:')

if Plan_Seleccionado == '1':
    plan = Plan_1[0]
elif Plan_Seleccionado == '2':
    plan = Plan_2[0]
elif Plan_Seleccionado == '3':
    plan = Plan_3[0]

if vehiculo == '1':
    precio = plan['Precio1']
elif vehiculo == '2':
    precio = plan['Precio2']

Registro_final = print(f'Su registro final es el {plan} por un precio de {precio} según su tipo de vehículo.')

if nombre_usuario not in historial_procesos:
    historial_procesos[nombre_usuario] = []
    historial_procesos[nombre_usuario].append(plan)

def nueva_eleccion ():
    if sig_proceso not in ['1', '2', '3']:
        print ('por favor digita el número correcto')
        sig_proceso = input ('1. nuevo registro\n2. Buscar procesos\n3. Salir del programa\n ¿Qué desea hacer?: ')