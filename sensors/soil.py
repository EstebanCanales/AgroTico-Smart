import time
from adafruit_seesaw.seesaw import Seesaw
from config import i2c

# -----------------------------
# 🧭 Inicialización del sensor
# -----------------------------
def init_soil_sensor(address=0x36):
    try:
        sensor = Seesaw(i2c, addr=address)
        print(f"[SoilSensor] Sensor inicializado correctamente en dirección 0x{address:02x}.")
        return sensor
    except Exception as e:
        print(f"[SoilSensor] Error al inicializar el sensor: {e}")
        return None

# -----------------------------
# 💧 Lectura de humedad y temperatura
# -----------------------------
def leer_soil_sensor(sensor):
    try:
        humedad = sensor.moisture_read()
        temperatura = sensor.get_temp()
        return humedad, temperatura
    except Exception as e:
        print(f"[SoilSensor] Error al leer datos: {e}")
        return None, None
