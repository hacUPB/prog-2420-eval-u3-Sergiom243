
print("Bienvenido a Lavafante")
vehiculo = input('Por favor indique de que tipo es su vehiculo\n1. Vehiculo convencional/carro \n2.Camioneta')

while vehiculo not in  ['1', '2']:
    print ('Por favor elija una opcion valida entre 1 carro y 2 camioneta')
    vehiculo = input('Por favor indique de que tipo es su vehiculo\n1. Vehiculo convencional/carro \n2.Camioneta: ')

print("Muchas gracias por seleccionar, estos son los planes que puede seleccionar para el lavado de su carro")




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
        print(f"Plan#1 \nNombre del plan: {Lavado_1['Tipo 1']}, Descripcion: {Lavado_1['Descripción']}, Precio de Carros: {Lavado_1['Precio1']}, Precio Camionetas {Lavado_1['Precio2']}")

    for Lavado_2 in Plan_2:
        print(f"Plan#2 \nNombre del plan: {Lavado_2['Tipo 2']}, Descripción: {Lavado_2['Descripción']}, Precio Carros: {Lavado_2['Precio1']}, Precio Camionetas: {Lavado_2['Precio2']}")

    for Lavado_3 in Plan_3:
        print(f"Plan#3 \nNombre del plan: {Lavado_3['Tipo 3']}, Descripción: {Lavado_3['Descripción']}, Precio Carros: {Lavado_3['Precio1']}, Precio Camionetas: {Lavado_3['Precio2']}")


registro_lavado()

Plan_Seleccionado = input('Despues de revisar los planes y precio según su vehiculo por favor elija el que mas desee\n1. Plan#1\n2. Plan#2\n3. Plan#3')

while Plan_Seleccionado not in ['1', '2', '3']:
    print('Por favor elija el numero del plan que desee correctamente')
    Plan_Seleccionado = input('Despues de revisar los planes y precio según su vehiculo por favor elija el que mas desee\n1. Plan#1\n2. Plan#2\n3. Plan#3')