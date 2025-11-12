from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Robot:
    def __init__(self, left_motor, right_motor,wheel_diameter, axle_track):
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
        self.hub = PrimeHub()
        self.drive_base.use_gyro(True)

    #Movimiento
    def straight(self, distance):
        self.drive_base.straight(distance)

    def turn(self, angle):
        self.drive_base.turn(angle)

    #Sonido
    def beep(self, freq, duration):
        self.hub.speaker.beep(freq, duration)

    def play_notes(self, notes):
        self.hub.speaker.play_notes(notes)

    #Luces
    def light_off(self):
        self.hub.light.off()

    def light_blink(self, color, durations):
        self.hub.light.blink(color, durations)

    def light_animate(self, colors, interval):
        self.hub.light.animate(colors, interval)
        

        

