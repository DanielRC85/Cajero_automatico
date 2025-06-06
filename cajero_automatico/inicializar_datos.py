import json
import os

RUTA_DATOS = os.path.join(os.path.dirname(__file__), 'datos', 'cuentas.json')

def inicializar_archivo_json():
    """Inicializa el archivo JSON si no existe."""
    if not os.path.exists(RUTA_DATOS):
        with open(RUTA_DATOS, 'w') as archivo:
            json.dump([], archivo)  # Inicializa con una lista vacía
