import serial
import json

# -----------------------------
# 🔌 Inicializar conexión serie
# -----------------------------
def init_serial(port="/dev/ttyACM0", baudrate=115200, timeout=2):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"[Serial] Puerto {port} abierto a {baudrate} bps.")
        return ser
    except serial.SerialException as e:
        print(f"[Serial] Error al abrir puerto: {e}")
        return None

# -----------------------------
# 📥 Leer una línea del puerto
# -----------------------------
def leer_serial_linea(ser):
    if ser and ser.is_open:
        try:
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            if linea.startswith("{") and linea.endswith("}"):
                return json.loads(linea)  # ✅ Convierte texto a dict
            else:
                print(f"[ESP32-S3] Línea no válida: {linea}")
        except json.JSONDecodeError as e:
            print(f"[ESP32-S3] Error parseando línea serial: {e}")
        except Exception as e:
            print(f"[Serial] Error al leer: {e}")
    else:
        print("[Serial] Puerto no está abierto.")
    return None
