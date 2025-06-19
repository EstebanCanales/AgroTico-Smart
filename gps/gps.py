import time
import serial
import adafruit_gps

def init_gps():
    uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)
    gps = adafruit_gps.GPS(uart, debug=False)
    gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')  # GGA y RMC
    time.sleep(1)
    gps.send_command(b'PMTK220,1000')  # Actualización cada 1s
    print("[GPS] GPS inicializado correctamente.")
    return gps

def leer_lat_lon(gps):
    try:
        gps.update()
    except Exception as e:
        print(f"[GPS] Error: {e}")
        return {"lat": 9.970220, "lon": -84.017793}  

    if not gps.has_fix:
        print("[GPS] No fix")
        return {"lat": 9.970220, "lon": -84.017793}  

    return {
        "lat": gps.latitude,
        "lon": gps.longitude
    }