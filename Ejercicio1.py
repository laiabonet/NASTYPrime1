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


if r1.sensor("color").color() == Color.RED:
    r1.beep(250, 1000)
    r1.turn(-90)
    r1.straight(830)


if r1.sensor("color").color() == Color.YELLOW:
    r1.beep(750, 1000)
    r1.turn(-90)
    r1.straight(830)

if r1.sensor("color").color() == Color.BLUE:
    r1.beep(1000, 1000)
    r1.turn(-90)
    r1.straight(830)

if r1.sensor("color").color() == Color.GREEN: 
    r1.beep(500, 1000)
    r1.turn(-90)
    r1.straight(830)
   


"""
sonidos = {
    Color.RED: 250,
    Color.BLUE: 1000,
    Color.GREEN: 500,
    Color.YELLOW: 750,
}
"""
