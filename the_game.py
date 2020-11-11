import pygame
import sys
pygame.init()

# pygame default window parameters
gameWindow = pygame.display.set_mode((500, 500))
pygame.display.set_caption('First Game')

# player and enemy parameters
x = 50
y = 50
width = 40
height = 60
velocity = 10

# colors
RED = 255, 0, 0
BLACK = 0, 0, 0

# main game loop
while True:

    # FPS
    pygame.time.delay(100)

    # quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # list of key press events
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocity

    if keys[pygame.K_RIGHT]:
        x += velocity

    if keys[pygame.K_UP]:
        y -= velocity

    if keys[pygame.K_DOWN]:
        y += velocity

    # redraws screen on refresh
    gameWindow.fill((BLACK))
    # draws game window
    pygame.draw.rect(gameWindow, (RED), (x, y, width, height))
    # this will update the window
    pygame.display.update()

pygame.quit()
