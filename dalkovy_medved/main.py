from src.constants import WIDTH, HEIGHT, BLACK
from src.get_joystick import get_joystick
from src.get_robot import get_robot

from pygame.locals import *

import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
joystick = get_joystick()

(left_motor, right_motor) = get_robot('169.254.221.230')

max_speed = 100
steer_in_place = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

            # Joystick movement
            if event.type == JOYAXISMOTION:
                x_axis = joystick.get_axis(0)  # X-axis on the left stick

                left_trigger = (joystick.get_axis(4) + 1) / 2
                right_trigger = (joystick.get_axis(5) + 1) / 2

                steer_coefficient = 1 - abs(x_axis)
                full_speed = right_trigger - left_trigger

                if not steer_in_place:
                    if x_axis < 0:  # Turn left
                        left_motor.on(full_speed * steer_coefficient)
                        right_motor.on(full_speed)
                    else:  # Turn right
                        left_motor.on(full_speed)
                        right_motor.on(full_speed * steer_coefficient)

            # Joystick buttons
            if event.type == JOYBUTTONDOWN:
                if joystick.get_button(2):
                    steer_in_place = True
            elif event.type == JOYBUTTONUP:
                if joystick.get_button(2):
                    steer_in_place = False

        # Fill the screen with black
        screen.fill(BLACK)

        # Update the display
        pygame.display.flip()

pygame.quit()
