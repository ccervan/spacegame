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

# Movement of the ship

playerX_change = 0


def player(x, y):
    # Method to draw on the screen
    screen.blit(playerImg, (x, y))


# Game loop: to keep the window open until user decides to close it

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If key stroke is pressed check if it is right or left

        # Move ship when pressing keys

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Background color of screen. Takes RGB values

    screen.fill((24, 18, 108))

    # Calling player funct to avoid it to disappear

    playerX += playerX_change
    player(playerX, playerY)

    # Always update display when adding something new

    pygame.display.update()