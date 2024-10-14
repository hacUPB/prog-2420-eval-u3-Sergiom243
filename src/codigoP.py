# Inicialización
print("Bienvenido a Lavafante")
historial_procesos = {}

def seleccionar_vehiculo():
    vehiculo = input('1. Vehículo convencional/carro \n2. Camioneta\nPor favor indique de qué tipo es su vehículo: ')
    while vehiculo not in ['1', '2']:
        print('Por favor elija una opción válida entre 1 carro y 2 camioneta')
        vehiculo = input('1. Vehículo convencional/carro \n2. Camioneta\nPor favor indique de qué tipo es su vehículo: ')
    return vehiculo

def registro_lavado():
    # Planes de lavado
    Plan_1 = {
        "Tipo": "Lavado básico",
        "Descripción": "Lavado de carrocería con shampoo encerado básico",
        "Precio1": 30000,
        "Precio2": 38000
    }

    Plan_2 = {
        "Tipo": "Lavado extra",
        "Descripción": "Lavado de carrocería, tapicería y asientos",
        "Precio1": 55000,
        "Precio2": 65000
    }

    Plan_3 = {
        "Tipo": "Lavado Premium",
        "Descripción": "Lavado completo, motor, rines, neumáticos y encerado premium",
        "Precio1": 85000,
        "Precio2": 95000
    }

    # Mostrar detalles de los planes
    print(f"Plan#1 \nNombre del plan: {Plan_1['Tipo']}, Descripción: {Plan_1['Descripción']}, Precio para Carros: {Plan_1['Precio1']}, Precio para Camionetas: {Plan_1['Precio2']}")
    print(f"Plan#2 \nNombre del plan: {Plan_2['Tipo']}, Descripción: {Plan_2['Descripción']}, Precio para Carros: {Plan_2['Precio1']}, Precio para Camionetas: {Plan_2['Precio2']}")
    print(f"Plan#3 \nNombre del plan: {Plan_3['Tipo']}, Descripción: {Plan_3['Descripción']}, Precio para Carros: {Plan_3['Precio1']}, Precio para Camionetas: {Plan_3['Precio2']}")

    return Plan_1, Plan_2, Plan_3

def seleccionar_plan(vehiculo):
    Plan_1, Plan_2, Plan_3 = registro_lavado()

    Plan_Seleccionado = input('1. Plan#1\n2. Plan#2\n3. Plan#3\nDespués de revisar los planes y precios según su vehículo, por favor elija el que más desee: ')
    while Plan_Seleccionado not in ['1', '2', '3']:
        print('Por favor elija el número del plan correctamente')
        Plan_Seleccionado = input('1. Plan#1\n2. Plan#2\n3. Plan#3\nDespués de revisar los planes y precios según su vehículo, por favor elija el que más desee: ')

    # Selección del plan y asignación de precio
    if Plan_Seleccionado == '1':
        plan = Plan_1
    elif Plan_Seleccionado == '2':
        plan = Plan_2
    elif Plan_Seleccionado == '3':
        plan = Plan_3

    if vehiculo == '1':
        precio = plan['Precio1']
    elif vehiculo == '2':
        precio = plan['Precio2']

    # Registro final
    print(f'Su registro final es el {plan["Tipo"]} por un precio de {precio} según su tipo de vehículo.')
    return plan

def guardar_en_historial(nombre_usuario, plan):
    if nombre_usuario not in historial_procesos:
        historial_procesos[nombre_usuario] = []
    historial_procesos[nombre_usuario].append(plan)

def buscar_procesos_por_nombre():
    nombre_buscar = input("Ingrese el nombre para buscar procesos: ")
    if nombre_buscar in historial_procesos:
        print(f"Procesos realizados para {nombre_buscar}:")
        for proceso in historial_procesos[nombre_buscar]:
            print(proceso)
    else:
        print(f"No se encontraron procesos para el nombre {nombre_buscar}")

def nueva_eleccion():
    # Preguntar al usuario qué quiere hacer a continuación
    sig_proceso = input('\n1. Nuevo registro\n2. Buscar procesos\n3. Salir del programa\n¿Qué desea hacer?: ')
    
    while sig_proceso not in ['1', '2', '3']:
        print('Por favor elija una opción válida')
        sig_proceso = input('\n1. Nuevo registro\n2. Buscar procesos\n3. Salir del programa\n¿Qué desea hacer?: ')

    if sig_proceso == '1':
        iniciar_registro()  # Llama a la función principal para empezar de nuevo
    elif sig_proceso == '2':
        buscar_procesos_por_nombre()
        nueva_eleccion()  # Después de buscar procesos, vuelve a preguntar qué desea hacer
    elif sig_proceso == '3':
        print("Gracias por su preferencia. El proceso ha finalizado.")
        exit()  # Finaliza el programa

# Función principal para iniciar el registro
def iniciar_registro():
    nombre_usuario = input("Por favor ingrese su nombre: ")  # Pedir el nombre cada vez
    vehiculo = seleccionar_vehiculo()
    plan = seleccionar_plan(vehiculo)
    guardar_en_historial(nombre_usuario, plan)
    nueva_eleccion()

# Iniciar el primer registro
iniciar_registro()

