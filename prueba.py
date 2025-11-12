from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=171)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
#drive_base.straight(300)
#drive_base.turn(90)
#drive_base.straight(300)
#drive_base.turn(90)
#drive_base.straight(300)
#drive_base.turn(90)
#drive_base.straight(300)
#drive_base.turn(90)
print("hola")

hub = PrimeHub()
#hub.light.animate([Color.VIOLET, Color.MAGENTA, Color.CYAN, Color.NONE], interval=2000)
#hub.light.animate([Color(h=i*8)for i in range(45)],interval=40)
#hub.display.icon(Icon.HAPPY)
#hub.speaker.beep(frequency=800, duration=1000)
#wait(10000)
hub.speaker.play_notes(["C4/4", "C4/4","G4/4","G4/4","A4/4","A4/4","G4/4","F4/4","F4/4","G4/4"])
