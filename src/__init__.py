def agregar_registro_usuario(nombre, vehiculo, plan, precio):
    if nombre not in registro_usuarios:
        registro_usuarios[nombre] = []
    registro_usuarios[nombre].append({
        'vehiculo': vehiculo,
        'plan': plan,
        'precio': precio
    })

def mostrar_registros_usuario(nombre):
    if nombre in registro_usuarios:
        print(f"\nRegistros de lavado para {nombre}:")
        for i, registro in enumerate(registro_usuarios[nombre], 1):
            print(f"Registro {i}: Vehículo: {registro['vehiculo']}, Plan: {registro['plan']}, Precio: {registro['precio']}")
    else:
        print(f"\nNo se encontraron registros para {nombre}.")

# Bucle principal
while True:
    accion = repetir_o_leer(nombre_usuario)

    if accion == 'registrar':
        vehiculo = input('Por favor indique de qué tipo es su vehículo\n1. Vehículo convencional/carro \n2. Camioneta: ')
        while vehiculo not in ['1', '2']:
            print('Por favor elija una opción válida.')
            vehiculo = input('1. Vehículo convencional/carro \n2. Camioneta: ')

        Plan_Seleccionado = input('Seleccione su plan:\n1. Plan#1\n2. Plan#2\n3. Plan#3: ')
        while Plan_Seleccionado not in ['1', '2', '3']:
            print('Opción no válida.')
            Plan_Seleccionado = input('Seleccione su plan:\n1. Plan#1\n2. Plan#2\n3. Plan#3: ')

        # Asignar el plan seleccionado
        if Plan_Seleccionado == '1':
            plan = Plan_1[0]
        elif Plan_Seleccionado == '2':
            plan = Plan_2[0]
        elif Plan_Seleccionado == '3':
            plan = Plan_3[0]

        # Asignar el precio en base al tipo de vehículo
        precio = plan['Precio1'] if vehiculo == '1' else plan['Precio2']
        
        # Guardar el registro
        agregar_registro_usuario(nombre_usuario, vehiculo, plan['Tipo'], precio)
        print(f"\nRegistro guardado: {plan['Tipo']} por un precio de {precio}.\n")

    elif accion == 'leer':
        mostrar_registros_usuario(nombre_usuario)

    continuar = input("\n¿Deseas realizar otra operación? (S/N): ").lower()
    if continuar != 's':
        break

print("\nGracias por usar Lavafante!")
