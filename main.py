import pygame

# always initialize pygame
pygame.init()
# create the screen and it needs two parameters: width and height
screen = pygame.display.set_mode((900, 600))

# Title and icon
pygame.display.set_caption("Space Ship")
icon = pygame.image.load("img/launch.png")
pygame.display.set_icon(icon)

# Game loop: to keep the window open until user decides to close it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background color of screen Tekes RGB values
    screen.fill((24, 18, 108))
    # Always update display when adding something new
    pygame.display.update()