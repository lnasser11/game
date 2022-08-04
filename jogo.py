import pygame
# INITIALIZE PYGAME
pygame.init()

# FPS
FPS = 60
clock = pygame.time.Clock()
contador = 200
# COLOURS 
WHITE = (255, 255, 255)
# FONTS
font = pygame.font.Font("PNG/galaxia.otf", 37)


# CREATE A DISPLAY SURVACE AND SET ITS CAPTIONS
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('OVER-Q')

# LOAD IMAGES
overq = pygame.image.load("OVER-Q/OVERQLOGO.png")
overq_rect = overq.get_rect()
overq = pygame.transform.scale(overq, (1000, 600))
overq_rect.topleft = (0,0)

background = pygame.image.load("OVER-Q/fundo.jpg")
background_rect = background.get_rect()
background = pygame.transform.scale(background, (600, 300))
background_rect.topleft = (0,0)

INICIO_text = font.render("titulo", True, WHITE)
INICIO_rect = INICIO_text.get_rect()
INICIO_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 30)

INICIO_text2 = font.render("APERTE 'ESPACO' PARA COMECAR", True, WHITE)
INICIO_rect2 = INICIO_text2.get_rect()
INICIO_rect2.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 10)

# GAME LOOP
estado = 'INTRO'
running = True 
while running:
    # --------------------------------- INTRO --------------------------------- #
    if estado == 'INTRO':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        contador -= 1
        print(contador)
        display_surface.blit(overq, overq_rect)
        if contador <= 0:
            estado = 'INICIO'
    # --------------------------------- TITLE SCREEN --------------------------------- #
    if estado == 'INICIO':
        display_surface.blit(background, background_rect)
        display_surface.blit(INICIO_text, INICIO_rect)
        display_surface.blit(INICIO_text2, INICIO_rect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                estado = 'JOGANDO'




    # FIM DE JOGO
    pygame.display.update()
    clock.tick(FPS)


# END OF THE GAME
pygame.quit()