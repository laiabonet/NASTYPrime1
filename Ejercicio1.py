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
#   3 N 4
#     O
#   1 S
#
freq = {
    Color.RED:250,
    Color.YELLOW:750,
    Color.BLUE:1000,
    Color.GREEN:500,
}

movimientos = {
    Color.RED:[ ["turn", [-90]],["straight", [830]] ],
    Color.BLUE:[ ["turn", [-90]],["straight", [830]] ],
    Color.YELLOW:[ ["turn", [-90]],["straight", [830]] ],
    Color.GREEN:[ ["turn", [-90]],["straight", [830]] ],
}


while True:
    sensor = r1.sensor("color").color()
    print(sensor)
    r1.beep(freq[sensor], 1000)
    r1.hacer_historia(movimientos.get(sensor,[]))

    


