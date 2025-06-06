import json
import os


def cargar_datos():
    """Carga los datos de cuentas desde un archivo JSON."""
    if not os.path.exists('datos/cuentas.json'):
        return []  # Retorna una lista vacía si el archivo no existe

    with open('datos/cuentas.json', 'r') as archivo:
        return json.load(archivo)


def guardar_datos(cuentas):
    """Guarda los datos de cuentas en un archivo JSON."""
    if not os.path.exists('datos'):
        os.makedirs('datos')  # Crea el directorio si no existe

    with open('datos/cuentas.json', 'w') as archivo:
        json.dump(cuentas, archivo, indent=4)

