from cajero.operaciones import iniciar_sesion, crear_cuenta

def menu_principal():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        print("\n--- Cajero Automático ---")
        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            crear_cuenta()
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
