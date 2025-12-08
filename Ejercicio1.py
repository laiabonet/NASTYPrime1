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
    #RED
    

    (Color.RED,1,"Norte"):[ [], 1, "Norte"],
    (Color.RED,2,"Norte"):[[ ["turn", [-90]],["straight", [830]],["turn", [-90]] ],1, "Oeste"],
    (Color.RED,3,"Norte"):[[ ["turn", [180]],["straight", [830]], ["turn", [180]] ],1, "Sur"],
    (Color.RED,4,"Norte"):[[ ["turn", [-90]],    ["straight", [830]],["turn", [-90]],["straight", [830]],["turn", [180]] ],1, "Norte"],
   
    #YELLOW
    (Color.YELLOW,1,"Norte"):[[ ["turn", [90]],["straight", [830]],["turn", [-90]] ],1, "Norte"],
    (Color.YELLOW,2,"Norte"):[ [], 2, "Norte"],
    (Color.YELLOW,3,"Norte"):[[ ["turn", [90]],["straight", [830]],["turn",[90]],["straight",[830]] ],1, "Norte"],
    (Color.YELLOW,4,"Norte"):[[ ["turn", [180]],["straight", [830]] ],1, "Norte"],
   
    #GREEN
    (Color.GREEN,1,"Norte"):[[ ["straight", [830]] ],3, "Norte"],
    (Color.GREEN,2,"Norte"):[[ ["straight", [830]],["turn",[-90]],["straight",[830]],["turn",[90]] ],3, "Norte"],
    (Color.GREEN,3,"Norte"):[ [], 3, "Norte"],
    (Color.GREEN,4,"Norte"):[[ ["turn", [-90]],["straight", [830]],["turn",[90]] ],3, "Norte"],

    #BLUE
    (Color.BLUE,1,"Norte"):[[ ["straight", [830]],["turn",[90]],["straight",[830]],["turn",[-90]] ],4, "Norte"],
    (Color.BLUE,2,"Norte"):[[ ["straight", [830]]],4, "Norte"],
    (Color.BLUE,3,"Norte"):[[ ["turn",[90]],["straight",[830]],["turn",[-90]] ],4, "Norte"],
    (Color.BLUE,4,"Norte"):[ [], 4, "Norte"],
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

    


