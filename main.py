import pygame
import random
import math

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

enemyX = random.randint(0, 836)
enemyY = random.randint(50, 110)
enemyX_change = 0.2
enemyY_change = 40

# Bullet

bulletImg = pygame.image.load("img/bullet.png")

# Ready state is when bullet can't be seen, ready to shoot
# Fire state is when bullet has been shoot

bulletX = 0
bulletY = 490
bulletX_change = 0
# Speed of bullet
bulletY_change = 4
bulletState = "ready"

score = 0


def player(x, y):
    # Method to draw on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    # Method to draw on the screen
    screen.blit(enemyImg, (x, y))


def fire(x, y):
    global bulletState
    bulletState = "fire"
    # To make the bullet appear on top of the ship
    screen.blit(bulletImg, (x + 16, y + 10))


# Function to calculate the distance between the bullet and the enemy to determine if they collided.
# Is the square root of (x1 - x2)^2 + (y1 - y2)^2
def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def destroy():
    global bulletY, bulletState, enemyX, enemyY, score
    bulletY = 490
    bulletState = "ready"
    score += 1
    print(score)
    enemyX = random.randint(0, 836)
    enemyY = random.randint(50, 110)

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
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletX = playerX
                    fire(bulletX, bulletY)

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

    # Bullet movement
    if bulletY <= 0:
        bulletY = 490
        bulletState = "ready"

    if bulletState == "fire":
        fire(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collided = collision(enemyX, enemyY, bulletX, bulletY)
    if collided:
        destroy()

    # Calling player function to avoid it to disappear
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Always update display when adding something new

    pygame.display.update()
