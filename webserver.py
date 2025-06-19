from flask import Flask, render_template, request, jsonify
import motors.stepper as stepper
import threading

app = Flask(__name__)
current_direction = None
control_lock = threading.Lock()

datos_globales = {}  # Variable global para almacenar el último JSON


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/datos", methods=["GET"])
def mostrar_datos():
    return jsonify(datos_globales)

@app.route("/mover", methods=["POST"])
def mover():
    global current_direction
    direccion = request.form.get("direccion")
    print(f"[DEBUG] Dirección recibida: {direccion}")
        
    with control_lock:
        current_direction = direccion
        
        if direccion == "adelante":
            stepper.move_forward()
        elif direccion == "atras":
            stepper.move_backward()
        elif direccion == "izquierda":
            stepper.move_left()
        elif direccion == "derecha":
            stepper.move_right()
        elif direccion == "parar":
            stepper.stop_motor()
        elif direccion == "subir":
            stepper.up_servo()
        elif direccion == "bajar":
            stepper.down_servo() 
    
    return render_template("mover.html", direccion=direccion)
    return "OK", 200

def get_current_direction():
    with control_lock:
        return current_direction