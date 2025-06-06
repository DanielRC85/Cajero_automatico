import json
import random
import string
import os


def cargar_datos():
    """Carga las cuentas desde un archivo JSON."""
    if os.path.exists('datos.json'):
        with open('datos.json', 'r') as file:
            return json.load(file)
    return []


def guardar_datos(cuentas):
    """Guarda las cuentas en un archivo JSON."""
    with open('datos.json', 'w') as file:
        json.dump(cuentas, file)


def generar_contraseña_aleatoria(tamaño=8):
    """Genera una contraseña aleatoria de un tamaño determinado."""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamaño))


def crear_cuenta():
    """Crea una nueva cuenta."""
    cuentas = cargar_datos()
    numero_cuenta = input("Ingrese su número de cuenta: ")

    # Verificar si la cuenta ya existe
    if any(c['numero_cuenta'] == numero_cuenta for c in cuentas):
        print("El número de cuenta ya existe. Intente con otro.")
        return

    contraseña = generar_contraseña_aleatoria()

    # Crear la cuenta con un saldo inicial de 0
    nueva_cuenta = {
        'numero_cuenta': numero_cuenta,
        'contraseña': contraseña,
        'saldo': 0
    }

    cuentas.append(nueva_cuenta)
    guardar_datos(cuentas)

    print(f"Cuenta creada con éxito. Número de cuenta: {numero_cuenta}, Contraseña: {contraseña}")

    # Sugerir al usuario que cambie la contraseña
    cambiar = input("¿Desea cambiar la contraseña aleatoria? (s/n): ").lower()
    if cambiar == 's':
        nueva_contraseña = input("Ingrese su nueva contraseña: ")
        nueva_cuenta['contraseña'] = nueva_contraseña
        guardar_datos(cuentas)  # Guarda los cambios en el archivo
        print("Contraseña cambiada con éxito.")


def iniciar_sesion():
    """Inicia sesión de un usuario existente."""
    cuentas = cargar_datos()
    usuario = input("Ingrese su número de cuenta: ")
    contraseña = input("Ingrese su contraseña: ")

    cuenta = next((c for c in cuentas if c['numero_cuenta'] == usuario and c['contraseña'] == contraseña), None)

    if cuenta:
        print(f"Bienvenido, {usuario}!")
        manejar_cuenta(cuenta, cuentas)
    else:
        print("Número de cuenta o contraseña incorrectos.")


def manejar_cuenta(cuenta_actual, cuentas):
    """Muestra las opciones disponibles para el usuario una vez que ha iniciado sesión."""
    while True:
        print("\n--- Opciones de la Cuenta ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Transferir dinero")
        print("5. Cambiar contraseña")
        print("6. Cerrar sesión")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print(f"Su saldo es: {cuenta_actual['saldo']} unidades.")
        elif opcion == '2':
            depositar_dinero(cuenta_actual)
        elif opcion == '3':
            retirar_dinero(cuenta_actual)
        elif opcion == '4':
            transferir_dinero(cuenta_actual, cuentas)
        elif opcion == '5':
            cambiar_contraseña(cuenta_actual)
        elif opcion == '6':
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def depositar_dinero(cuenta_actual):
    """Permite al usuario depositar dinero en su cuenta."""
    monto = float(input("Ingrese el monto a depositar: "))
    cuenta_actual['saldo'] += monto
    guardar_datos(cargar_datos())  # Actualiza el archivo JSON
    print(f"Se han depositado {monto} unidades. Su nuevo saldo es: {cuenta_actual['saldo']} unidades.")


def retirar_dinero(cuenta_actual):
    """Permite al usuario retirar dinero de su cuenta."""
    monto = float(input("Ingrese el monto a retirar: "))
    if monto > cuenta_actual['saldo']:
        print("Fondos insuficientes.")
    else:
        cuenta_actual['saldo'] -= monto
        guardar_datos(cargar_datos())  # Actualiza el archivo JSON
        print(f"Se han retirado {monto} unidades. Su nuevo saldo es: {cuenta_actual['saldo']} unidades.")


def transferir_dinero(cuenta_actual, cuentas):
    """Permite al usuario transferir dinero a otra cuenta existente."""
    numero_destino = input("Ingrese el número de cuenta destino: ")
    cuenta_destino = next((c for c in cuentas if c['numero_cuenta'] == numero_destino), None)

    if cuenta_destino is None:
        print("La cuenta destino no existe.")
        return

    monto = float(input("Ingrese el monto a transferir: "))
    if monto > cuenta_actual['saldo']:
        print("Fondos insuficientes.")
    else:
        cuenta_actual['saldo'] -= monto
        cuenta_destino['saldo'] += monto
        guardar_datos(cuentas)  # Actualiza el archivo JSON
        print(
            f"Se han transferido {monto} unidades a la cuenta {numero_destino}. Su nuevo saldo es: {cuenta_actual['saldo']} unidades.")


def cambiar_contraseña(cuenta_actual):
    """Permite al usuario cambiar su contraseña."""
    nueva_contraseña = input("Ingrese su nueva contraseña: ")
    cuenta_actual['contraseña'] = nueva_contraseña
    cuentas = cargar_datos()  # Carga las cuentas para actualizarlas
    for cuenta in cuentas:
        if cuenta['numero_cuenta'] == cuenta_actual['numero_cuenta']:
            cuenta['contraseña'] = nueva_contraseña
            break
    guardar_datos(cuentas)  # Guarda los cambios en el archivo
    print("Contraseña cambiada con éxito.")
