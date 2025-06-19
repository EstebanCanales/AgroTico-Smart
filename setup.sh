#!/bin/bash

# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate

# Actualizar pip
pip install --upgrade pip

echo "Instalando librerías de sensores Adafruit..."
pip install adafruit-circuitpython-bmp3xx
pip install adafruit-circuitpython-scd30
pip install adafruit-circuitpython-seesaw
pip install adafruit-circuitpython-ltr390

echo "Instalando librerías para bonnets..."
pip install adafruit-circuitpython-mcp230xx
pip install adafruit-circuitpython-motorkit
pip install adafruit-circuitpython-gps

echo "Instalando comunicación con hardware..."
pip install Adafruit-Blinka
pip install smbus2

echo "Instalando librerías de propósito general..."
pip install pandas
pip install requests

echo "✅ Instalación completada."
