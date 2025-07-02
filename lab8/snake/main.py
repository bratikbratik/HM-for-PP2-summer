import random
import time
import pygame

w, h = 400, 400

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

def game_over():
    screen.fill(BLACK)
    final_text = font.render(f"Game Over! Your Score: {score}", True, RED)
    screen.blit(final_text, (w // 4, h // 3))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

def generate_fruit_position():
    while True:
        pos = [random.randrange(1, (w // 10)) * 10, random.randrange(1, (h // 10)) * 10]
        if pos not in snake_body and 0 < pos[0] < w - 10 and 0 < pos[1] < h - 10:
            return pos

pygame.init()
screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()
snake_speed = 10

font = pygame.font.Font(None, 24)

snake_head = [w // 2, h // 2]
snake_body = [[w//2, h//2], [w//2-10, h//2], [w//2-20, h//2], [w//2-30, h//2]]
direction = "RIGHT"
change_to = direction

fruit_pos = generate_fruit_position()
fruit_spawn = True

score = 0
level = 1
foods_eaten = 0

Eating = True

while Eating:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    direction = change_to

    if direction == "UP":
        snake_head[1] -= 10
    elif direction == "DOWN":
        snake_head[1] += 10
    elif direction == "LEFT":
        snake_head[0] -= 10
    elif direction == "RIGHT":
        snake_head[0] += 10

    # Update body coordinates after movement of head 
    snake_body.insert(0, list(snake_head))
    if snake_head == fruit_pos:
        score += 10
        foods_eaten += 1
        fruit_spawn = False
    else:
        # Delete last useless coordinate
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = generate_fruit_position()
        fruit_spawn = True

    if foods_eaten > 2:
        level += 1
        snake_speed += 2
        foods_eaten = 0

    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw fruit by coordinate
    pygame.draw.rect(
        screen, RED, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10)
    )

    info_text = font.render(f"Score: {score} Level: {level}", True, WHITE)
    screen.blit(info_text, (10, 10))

    if (
        snake_head[0] < 0
        or snake_head[0] >= w
        or snake_head[1] < 0
        or snake_head[1] >= h
    ):
        game_over()
    
    for block in snake_body[1:]:
        if snake_head == block:
            game_over()

    pygame.display.update()
    clock.tick(snake_speed)