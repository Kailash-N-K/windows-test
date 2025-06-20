import pygame.mixer
from pygame.mixer import Sound
import os

pygame.mixer.init()

sound = Sound("mockingbird_speed_up.mp3")

sound.play()

os.system("pause")