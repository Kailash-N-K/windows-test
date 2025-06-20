from gpiozero import Robot, Motor
from time import sleep

robot = Robot(left=Motor(14, 15), right=Motor(23, 24))

try:
    while True:
        robot.forward()
        sleep(3)
        robot.stop()
        sleep(1)
        robot.backward()
        sleep(3)
        robot.stop()
        sleep(1)

except KeyboardInterrupt:
    robot.close()