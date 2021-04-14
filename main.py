import pygame

# always initialize pygame
pygame.init()
# create the screen and it needs two parameters: width and height
screen = pygame.display.set_mode((900, 600))

# Title and icon
pygame.display.set_caption("Space Ship")
icon = pygame.image.load("img/launch.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("img/battleship.png")
playerX = 395
playerY = 490


def player():
    # Method to draw on the screen
    screen.blit(playerImg, (playerX, playerY))


# Game loop: to keep the window open until user decides to close it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background color of screen. Takes RGB values
    screen.fill((24, 18, 108))

    # Calling player funct to avoid it to disappear
    player()

    # Always update display when adding something new
    pygame.display.update()