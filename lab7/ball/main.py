import pygame
import sys

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Red Ball Movement")

RADIUS = 25
ball_color = (255, 0, 0)
x, y = w // 2, h // 2

STEP = 20

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - STEP - RADIUS >= 0:
        x -= STEP
    if keys[pygame.K_RIGHT] and x + STEP + RADIUS <= w:
        x += STEP
    if keys[pygame.K_UP] and y - STEP - RADIUS >= 0:
        y -= STEP
    if keys[pygame.K_DOWN] and y + STEP + RADIUS <= h:
        y += STEP

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (x, y), RADIUS)
    pygame.display.flip()

