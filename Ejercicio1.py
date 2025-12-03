from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from robot import Robot

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
#ultrasonido = UltrasonicSensor(Port.D)
color = ColorSensor(Port.F)

r1 = Robot(left_motor, right_motor, 56, 170)
#r1.guardar_sensor("ultra",ultrasonido)
r1.guardar_sensor("color",color)

# Suponemos que el robot comienza en la esq 1. mirando al sur
#
#   3  4        Norte
#         Oeste        Este
#   1  2         Sur
#  ROJO ->  Ir a la esquina 1
#  VERDE -> Ir a la esquina 3
#  AZUL -> Ir a la esquina 4
#  AMARILLO -> Ir a la esquina 2

freq = {
    Color.RED:250,
    Color.YELLOW:750,
    Color.BLUE:1000,
    Color.GREEN:500,
}

movimientos = {
    (Color.RED,2,"Norte"):[[ ["turn", [-90]],["straight", [830]] ],1, "Oeste"],
    (Color.RED,2,"Sur"):[[["turn", [90]],["straight", [830]] ],1, "Oeste"],
    (Color.RED,2,"Oeste"):[[["straight", [830]] ],1,"Oeste"],
    (Color.RED,2,"Este"):[[["turn", [180]],["straight", [830]] ],1,"Oeste"],
    (Color.GREEN,1,"Oeste"):[[["turn", [90]],["straight",[830]] ],3, "Norte"],
    (Color.BLUE,3,"Norte"):[[["turn", [90]]
}

#Condiciones iniciales
esquina = 2
orientacion = "Norte"

while True:
    sensor = r1.sensor("color").color()
    key = (sensor,esquina,orientacion)
    historia, esquina, orientacion = movimientos.get(key ,[[], esquina,orientacion])

    print(key)
    r1.beep(freq[sensor], 1000)
    r1.hacer_historia(historia)

    


