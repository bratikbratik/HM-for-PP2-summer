from datetime import datetime
import pygame
import os

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

background = pygame.image.load("/Users/kamillakadyrbaeva/Desktop/PP2/lab7/mickey/clock.png")
min_hand = pygame.image.load("/Users/kamillakadyrbaeva/Desktop/PP2/lab7/mickey/min_hand.png")
sec_hand = pygame.image.load("/Users/kamillakadyrbaeva/Desktop/PP2/lab7/mickey/sec_hand.png")

original_sh_position = sec_hand.get_rect(center=(w // 2, h // 2))
original_mh_position = min_hand.get_rect(center=(w // 2, h // 2))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print("BYE!!!!!!")

    screen.blit(background, (0, 0))

    now = datetime.now()
    sec = now.second
    min = now.minute

    sec_angle = -6 * sec
    min_angle = -6 * min

    rotated_sh = pygame.transform.rotate(sec_hand, sec_angle)
    rotated_mh = pygame.transform.rotate(min_hand, min_angle)

    sh_rect = rotated_sh.get_rect(center=original_sh_position.center)
    mh_rect = rotated_mh.get_rect(center=original_mh_position.center)

    screen.blit(rotated_sh, sh_rect)
    screen.blit(rotated_mh, mh_rect)

    pygame.display.flip()
    clock.tick(60)