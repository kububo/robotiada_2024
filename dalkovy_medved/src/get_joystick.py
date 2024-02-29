import pygame


def get_joystick():
    pygame.joystick.init()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    return joystick
