# 🏧 **Cajero Automático – Simulación de Cajero Bancario en Python**

Proyecto en consola desarrollado con Python, que simula el comportamiento de un cajero automático. Incluye operaciones comunes como consulta de saldo, depósitos, retiros, transferencias, cambio de PIN y bloqueo de cuenta tras intentos fallidos.
Ideal como ejercicio práctico para afianzar estructuras de control, modularidad, funciones, validación y lógica de negocio.

---

## 🚀 **Características principales**

* Simulación realista del flujo de un cajero automático.
* Operaciones disponibles:

  * Inicio de sesión seguro mediante PIN.
  * Consulta de saldo.
  * Depósito de fondos.
  * Retiro de efectivo con validación de saldo.
  * Transferencias entre cuentas.
  * Cambio de PIN.
  * Bloqueo automático tras múltiples intentos de PIN fallido.
* Validaciones implementadas:

  * PIN incorrecto.
  * Saldo insuficiente.
  * Operaciones inválidas.
  * Control de intentos y seguridad básica.

---

## 🧰 **Tecnologías utilizadas**

* 🐍 **Python 3.x**
* Módulos estándar de Python (`os`, `json`, `getpass`, etc.)
* Programación modular (archivos separados por funcionalidades)
* Sin dependencias externas

---

## ⚙️ **Cómo ejecutar el proyecto**

1. Clona el repositorio:

```bash
git clone https://github.com/DanielRC696/CajeroAutomatic.git
cd CajeroAutomatic
```

2. Asegúrate de tener Python 3.x instalado:

```bash
python --version
```

3. Ejecuta el archivo principal:

```bash
python main.py
```

4. Sigue las instrucciones en pantalla para interactuar con el cajero.

---

## 📁 **Estructura del proyecto**

```
CajeroAutomatico/
├── main.py                # Lógica principal y flujo del cajero
├── accounts.py            # Gestión de usuarios y cuentas
├── transactions.py        # Funciones para depósitos, retiros, etc.
├── utils/                 # Funciones auxiliares (validaciones, entrada segura)
├── data/                  # Archivos JSON con información de prueba (si existen)
└── README.md              # Documento explicativo del proyecto
```

---

## 👤 **Desarrollador**

* **Nombre:** Daniel Augusto Romero Cortés
* **Email:** [romerocortesdaniel9@gmail.com](mailto:romerocortesdaniel9@gmail.com)
* **GitHub:** [@DanielRC85](https://github.com/DanielRC85)






