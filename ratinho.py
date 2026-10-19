# --------------- Imports ---------------

import sys, os, random
import pygame

# ---------------- Configurações ----------------

FPS = 60
W_SIZE = W_WIDTH, W_HEIGHT = 640, 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
W_BGCOLOR = WHITE
VELOCIDADE = 5

PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
path_rato = os.path.join(PASTA_DO_PROJETO, "rato.png")
path_queijo = os.path.join(PASTA_DO_PROJETO, "queijo.png")

pygame.init()

# define tamanho e título da janela
SCREEN = pygame.display.set_mode(W_SIZE)
pygame.display.set_caption('Jogo do ratinho')
clock = pygame.time.Clock()

# ---------------- Sprites ----------------

rato_esq = pygame.image.load(path_rato)
rato_esq = pygame.transform.scale(rato_esq, (60, 60))
rato_dir = pygame.transform.flip(rato_esq, True, False) 
rato = rato_esq

queijo = pygame.image.load(path_queijo)
queijo = pygame.transform.scale(queijo, (45, 45))

# captura os retângulos das imagens
rato_rect = rato.get_rect()
rato_rect.center = (W_WIDTH // 2, W_HEIGHT // 2)
queijo_rect = queijo.get_rect()

def trocar_lugar_queijo():
    x = random.randint(queijo_rect.width // 2, W_WIDTH - queijo_rect.width // 2)
    y = random.randint(queijo_rect.height // 2, W_HEIGHT - queijo_rect.height // 2)
    queijo_rect.center = (x, y)

trocar_lugar_queijo()
pontos = 0


# ---------------- Loop principal ----------------
while True:
    # captura os eventos da interface
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # captura uma tecla pressionada
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        rato_rect.move_ip(-VELOCIDADE, 0)
        rato = rato_esq
    if key[pygame.K_RIGHT]:
        rato_rect.move_ip(VELOCIDADE, 0)
        rato = rato_dir
    if key[pygame.K_UP]:
        rato_rect.move_ip(0, -VELOCIDADE)
    if key[pygame.K_DOWN]:
        rato_rect.move_ip(0, VELOCIDADE)

    # verifica colisao do rato com o queijo
    if rato_rect.colliderect(queijo_rect):
        pontos += 1
        print(f'{pontos} queijo comido!')
        trocar_lugar_queijo()

    # desenha tudo na tela
    SCREEN.fill(W_BGCOLOR)
    SCREEN.blit(queijo, queijo_rect)
    SCREEN.blit(rato, rato_rect)

    pygame.display.update()# atualiza a tela
    clock.tick(FPS)
