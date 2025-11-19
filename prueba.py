from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait
from robot import Robot

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)

r1 = Robot(left_motor, right_motor, 56, 170)

r1.straight(250)
r1.turn(90)
r1.straight(200)
r1.turn(-90)
r1.beep(800, 500)
r1.deshacer_historia()


#r1.light_blink(Color.VIOLET, [1000, 1000])
#wait(2000)
#r1.play_notes(["C4/4", "C4/4","G4/4","G4/4","A4/4","A4/4","G4/4","F4/4","F4/4","G4/4"])
#wait(10000)


# Drive forward by 500mm (half a meter).
#drive_base.straight(300)
#drive_base.turn(90)
#drive_base.straight(300)
#drive_base.turn(90)
#drive_base.straight(300)
#drive_base.turn(90)
#drive_base.straight(300)
#drive_base.turn(90)
#print("hola")

#hub = PrimeHub()
#hub.light.animate([Color.VIOLET, Color.MAGENTA, Color.CYAN, Color.NONE], interval=2000)
#hub.light.animate([Color(h=i*8)for i in range(45)],interval=40)
#hub.display.icon(Icon.HAPPY)
#hub.speaker.beep(frequency=800, duration=1000)
#wait(10000)
#hub.speaker.play_notes(["C4/4", "C4/4","G4/4","G4/4","A4/4","A4/4","G4/4","F4/4","F4/4","G4/4"])
