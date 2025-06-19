import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import RPi.GPIO as GPIO

# Inicializar el MotorKit (motor paso a paso)
kit = MotorKit(i2c=board.I2C())

# Configuración del servo
SERVO_PIN = 10  # GPIO10 (BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# PWM a 50 Hz (frecuencia estándar para servos)
servo_pwm = GPIO.PWM(SERVO_PIN, 50)
servo_pwm.start(0)

def set_angle(angle):
    """Mueve el servo MG90S al ángulo especificado (0 a 180 grados)."""
    # Conversión: 0° → 2.5%, 180° → 12.5%
    duty = 2.5 + (angle / 180.0) * 10
    servo_pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo_pwm.ChangeDutyCycle(0)  # Desactiva PWM para evitar vibración

def move_forward():
    for i in range(250):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        time.sleep(0.002)

def move_backward():
    for i in range(250):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
        time.sleep(0.002)

def move_left():
    for i in range(250):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
        time.sleep(0.002)

def move_right():
    for i in range(250):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
        time.sleep(0.002)

def down_servo():
    set_angle(90)  # Brazo hacia abajo

def up_servo():
    set_angle(0)  # Brazo hacia arriba (o medio)

def stop_motor():
    kit.stepper1.release()
    kit.stepper2.release()

def cleanup():
    servo_pwm.stop()
    GPIO.cleanup()
