
# FarmTech Programm 🌱

Un sistema modular para controlar sensores ambientales, motores y módulos GPS en aplicaciones agrícolas utilizando Raspberry Pi.

## 📦 Estructura del Proyecto
Este proyecto está organizado en las siguientes carpetas y archivos:

- **`gps/`**: Módulos de posicionamiento GPS (incluye la configuración y la lectura de datos GPS).
- **`interface/`**: Control de hardware externo, como expansores de GPIO y hubs (por ejemplo, el uso de `STEMMA`).
- **`motors/`**: Control de motores paso a paso y otros actuadores.
- **`sensors/`**: Sensores ambientales (como temperatura, luz UV, humedad, CO₂, presión atmosférica, etc.).
- **`utils/`**: Utilidades generales como `logger.py` y `debugger.py` para facilitar la depuración y el registro de datos.
- **`config.py`**: Configuración general para todo el sistema.
- **`main.py`**: Punto de entrada del programa que orquesta la ejecución del robot agrícola.

## 🛠 Requisitos

Este proyecto requiere los siguientes paquetes Python para funcionar correctamente:

```bash
pip install -r requirements.txt
```

Asegúrate de tener las siguientes librerías instaladas en tu entorno:

- `adafruit-circuitpython-bmp3xx`: Para sensores de presión barométrica.
- `adafruit-circuitpython-ltr390`: Para sensores de luz UV.
- `adafruit-circuitpython-scd30`: Para sensores de CO₂, temperatura y humedad.
- `RPi.GPIO`: Para interactuar con los pines GPIO de la Raspberry Pi.
- `numpy`: Para cálculos numéricos.

## 🧑‍💻 Cómo usar el proyecto

### 1. Configuración de software

Asegúrate de tener un entorno Python 3 instalado. Si no tienes `pip`, instálalo primero. Luego, instala las dependencias con:

```bash
pip install -r requirements.txt
```

### 2. Ejecutar el proyecto

Una vez todo esté configurado, puedes ejecutar el proyecto desde la terminal:

```bash
python3 main.py
```

El programa comenzará a leer los datos de los sensores y, dependiendo de la programación, tomará decisiones que afecten a los actuadores (motores, luces, etc.).



## 🛠️ Estructura de carpetas

```text
├── gps/
│   ├── gps.py
├── interface/
│   ├── gpio_expander.py
│   └── hubstemma.py
├── motors/
│   ├── stepper.py
├── sensors/
│   ├── bmp.py
│   ├── ltr390.py
│   ├── soil.py
│   └── scd30.py
├── utils/
│   ├── logger.py
│   └── debugger.py
├── config.py
└── main.py
```

## 📑 Contribuciones

1. Forkea el repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios.
4. Haz un commit de tus cambios (`git commit -am 'Agregada nueva característica'`).
5. Push al branch (`git push origin feature/nueva-caracteristica`).
6. Crea un Pull Request.

