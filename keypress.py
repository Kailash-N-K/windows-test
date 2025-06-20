import keyboard
from gpiozero import Robot, Motor
from time import sleep

robot = Robot(left=Motor(14, 15), right=Motor(24, 23))

try:
    while True:
        if keyboard.is_pressed("up"):
            robot.forward()

        elif keyboard.is_pressed("down"):
            robot.backward()

        elif keyboard.is_pressed("left"):
            robot.left()

        elif keyboard.is_pressed("right"):
            robot.right()

        else:
            robot.stop()

except KeyboardInterrupt:
    robot.close()