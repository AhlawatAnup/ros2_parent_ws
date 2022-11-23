import pygame

pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

# Prints the values for axis0
while True:
        pygame.event.pump()
        # print ("x axis: ", pygame.joystick.Joystick(0).get_axis(0))
        print ("y axis: ", -(pygame.joystick.Joystick(0).get_axis(4)))
        # print ("z axis: ", pygame.joystick.Joystick(0).get_axis(4))