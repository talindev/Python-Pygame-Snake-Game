# importar as bibliotecas
import pygame
import random

# inicializar pygame
pygame.init()

# declarações dos limites de espaço
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FOOD_X = random.randint(1,SCREEN_WIDTH - 50)
FOOD_Y = random.randint(1,SCREEN_HEIGHT - 50)
SQUARE_X = random.randint(1,SCREEN_WIDTH - 50)
SQUARE_Y = random.randint(1,SCREEN_HEIGHT - 50)

# fontes e textos
font = pygame.font.Font('freesansbold.ttf', 32)

none = font.render('', True, (40,40,40))
none_square = none.get_rect()
none_square.centerx = SCREEN_WIDTH // 2
none_square.top = 10

congrats = font.render('CONGRATS!', True, (0,0,255))
congrats_square = congrats.get_rect()
congrats_square.centerx = SCREEN_WIDTH // 2
congrats_square.top = 10

# sistema de score
score_value = 0
score = font.render(str(score_value), True, (255,255,255),)
score_square = score.get_rect()

# para checagem do spawn do texto de parabéns aos 10 pontos
congrats_spawn = False

# checagem de spawn da comida
food_spawn = True

# aleatorização da posição
def random_pos():
    return random.randint(1,1000), random.randint(1,1000)

# declaração da janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# estrutura retangular dos 2 elementos principais (cobra e comida)
square = pygame.Rect((SQUARE_X,SQUARE_Y,50,50))
food = pygame.Rect((FOOD_X,FOOD_Y,50,50))

# array de segmentos para incremento do corpo da cobra
segments = [square.copy()]
length = 1


# ÁREA DE TESTE OU RASCUNHO
# square_center = square.copy()
# food_center = food.copy()

# declaração de cor 'color'
color = (0,255,0)

# loop do jogo
run = True
while run:

    # preenchimento de tela para não bugar os segmentos
    screen.fill((40,40,40))

    # inserção das fontes e textos
    none_square = none.get_rect(centerx=SCREEN_WIDTH // 2, top=10)
    congrats_square = congrats.get_rect(centerx=SCREEN_WIDTH // 2, top=10)

    # inserção do sistema de score
    score = font.render('score: ' + str(score_value), True, (255, 255, 255), )
    screen.blit(score, score_square)

    # desenho da cobra
    for segment in segments:
        pygame.draw.rect(screen, color, segment)
    pygame.draw.rect(screen, (255, 0, 0), food)

    # sistema de pressionamento de teclas e movimentação do jogador
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        square.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        square.move_ip(0, 1)
    elif key[pygame.K_a] == True:
        square.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        square.move_ip(1, 0)

    segments.append(square.copy()) # adição de quadrados novos no array por meio do comando 'append'


    segments = segments[-length:] # Em Python, o operador de slicing [:] permite obter uma sublista de uma lista.
                                  # segments[-length:] usa índices negativos. Em Python, um índice negativo começa do final da lista,
                                  # com -1 sendo o último elemento, -2 sendo o penúltimo, e assim por diante.
                                  # segments[-length:] significa "pegue os últimos 'length' elementos da lista 'segments'".
                                  # Isso garante que, independentemente do número de segmentos adicionados,
                                  # apenas os 'length' segmentos mais recentes sejam mantidos na lista.

    if segments[0].colliderect(food): # checagem de colisão para incrementar a cobra, aumentando o score e adicionando os valores para o array
        FOOD_X, FOOD_Y = random_pos()
        food.topleft = (FOOD_X, FOOD_Y)
        score_value += 1
        length += 50

    if score_value == 10: # ativação da mensagem de parabéns
        screen.blit(congrats, congrats_square)
        congrats_spawn = True

    if congrats_spawn == True: # desativação da mensagem de parabéns
        screen.blit(none, none_square)
        congrats_spawn = False

    for event in pygame.event.get(): # evento de fechar o jogo
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() # atualização dos conteúdos do jogo

pygame.quit()
