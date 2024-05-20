# lets develop a snake game in python using pygame module
# import pygame
import pygame
import time
import random
# initialize the pygame
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
