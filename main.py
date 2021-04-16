import pygame
import random

# always initialize pygame
pygame.init()

# create the screen and it needs two parameters: width and height
screen = pygame.display.set_mode((900, 600))

# Background image
background = pygame.image.load("img/stars.jpg")

# Title and icon
pygame.display.set_caption("Space Ship")
icon = pygame.image.load("img/launch.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("img/spaceship.png")
playerX = 395
playerY = 490
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("img/ufo.png")

# Use random library to make enemy appear in random places

enemyX = random.randint(0, 800)
enemyY = random.randint(50, 110)
enemyX_change = 0.2
enemyY_change = 40


def player(x, y):
    # Method to draw on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    # Method to draw on the screen
    screen.blit(enemyImg, (x, y))

# Game loop: to keep the window open until user decides to close it


running = True
while running:
    # Background color of screen. Takes RGB values
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If key stroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Movement of ship
    playerX += playerX_change

    # Boundaries for the ship on screen

    if playerX <= 0:
        playerX = 0
    elif playerX >= 836:
        playerX = 836

    # Movement of enemy
    enemyX += enemyX_change

    # Boundaries for enemy
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 836:
        enemyX_change = -0.2
        enemyY += enemyY_change

    # Calling player function to avoid it to disappear

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Always update display when adding something new

    pygame.display.update()