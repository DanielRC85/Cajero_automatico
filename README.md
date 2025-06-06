# 🏧 Cajero Automatic – Simulación de Cajero Bancario en Python

Proyecto de consola en Python que simula el funcionamiento de un cajero automático. Permite operar con cuentas bancarias: consultar saldo, depositar, retirar dinero, transferencias, cambio de PIN y bloqueo de cuenta. Ideal como ejercicio didáctico de estructuras de control, funciones y manejo de datos.

---

## 🚀 Características

- Simulación completa de un cajero automático en consola.
- Funciones disponibles:
  - Inicio de sesión seguro (PIN).
  - Consultar saldo.
  - Depositar fondos.
  - Retirar efectivo.
  - Transferencias entre cuentas.
  - Cambio de PIN.
  - Bloqueo de cuenta tras múltiples intentos fallidos.
- Manejo de errores y validaciones (saldo insuficiente, PIN incorrecto, operaciones inválidas).

---

## 🧰 Tecnologías

- Python 3.x
- Módulos estándar (no se requieren dependencias externas)

---

## ⚙️ Instalación y uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/DanielRC696/CajeroAutomatic.git
   cd CajeroAutomatic
2. Verifica que tengas Python 3.x instalado:
python --version

3. Ejecuta la aplicación:
python main.py

4. Sigue las instrucciones en pantalla para interactuar con el cajero

📁 Estructura del proyecto
CajeroAutomatic/
├── main.py                # Lógica principal del cajero
├── accounts.py            # Gestión de cuentas y usuarios
├── transactions.py        # Funciones para operaciones bancarias
├── utils/                 # Funciones auxiliares (validaciones, input)
├── data/                  # Archivos JSON o datos de ejemplo (si existen)
└── README.md              # Este archivo explicativo

📫 Contacto
Proyecto creado por: Daniel Augusto Romero Cortes
📧 romerocortesdaniel9@gmail.com
🇨🇴 Colombia

📌 Nota
Este README está pensado para comandos en consola. Si luego agregas interfaz gráfica, API, web o móvil, adapta el README en consecuencia.


