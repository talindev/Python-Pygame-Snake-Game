import pygame
import random

pygame.init()

FOOD_X = random.randint(1,850)
FOOD_Y = random.randint(1,850)
SQUARE_X = random.randint(1,850)
SQUARE_Y = random.randint(1,850)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# FONTES

font = pygame.font.Font('freesansbold.ttf', 32)

none = font.render('', True, (40,40,40))
none_square = none.get_rect()
none_square.centerx = SCREEN_WIDTH // 2
none_square.top = 10

congrats = font.render('CONGRATS!', True, (0,0,255))
congrats_square = congrats.get_rect()
congrats_square.centerx = SCREEN_WIDTH // 2
congrats_square.top = 10

score_value = 0
score = font.render(str(score_value), True, (255,255,255),)
score_square = score.get_rect()

congrats_spawn = False

# CHECAGEM DA COMIDA

food_spawn = True


def random_pos():
    return random.randint(1,1000), random.randint(1,1000)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

square = pygame.Rect((SQUARE_X,SQUARE_Y,50,50))
food = pygame.Rect((FOOD_X,FOOD_Y,50,50))

segments = [square.copy()]
length = 1

# square_center = square.copy()
# food_center = food.copy()

color = (0,255,0)

run = True
while run:

    screen.fill((40,40,40))

    none_square = none.get_rect(centerx=SCREEN_WIDTH // 2, top=10)
    congrats_square = congrats.get_rect(centerx=SCREEN_WIDTH // 2, top=10)

    score = font.render('score: ' + str(score_value), True, (255, 255, 255), )
    screen.blit(score, score_square)

    for segment in segments:
        pygame.draw.rect(screen, color, segment)
    pygame.draw.rect(screen, (255, 0, 0), food)

    if segments[0].colliderect(food) == 1:
        color = (0,0,255)
    else:
        color = (0,255,0)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        square.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        square.move_ip(0, 1)
    elif key[pygame.K_a] == True:
        square.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        square.move_ip(1, 0)

    segments.append(square.copy())
    segments = segments[-length:]

    if segments[0].colliderect(food):
        FOOD_X, FOOD_Y = random_pos()
        food.topleft = (FOOD_X, FOOD_Y)
        score_value += 1
        length += 50

    if score_value == 10:
        screen.blit(congrats, congrats_square)
        congrats_spawn = True

    if congrats_spawn == True:
        screen.blit(none, none_square)
        congrats_spawn = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()