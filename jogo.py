import pygame
# INITIALIZE PYGAME
pygame.init()

# FPS
FPS = 60
clock = pygame.time.Clock()
contador_intro = 10
contador_intro_2 = 10
contador_intro_3 = 10
# COLOURS 
WHITE = (255, 255, 255)
DARK_BLUE = (32, 42, 67)
# FONTS
intro_font = pygame.font.Font("galaxia.otf", 70)
font = pygame.font.Font("galaxia.otf", 37)
font_title = pygame.font.Font("galaxia.otf", 150)
over_q = pygame.font.Font("overq_font.ttf", 100)
mebeo = pygame.font.Font("mebeo_true.ttf", 100)


# CREATE A DISPLAY SURVACE AND SET ITS CAPTIONS
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('OVER-Q')

# LOAD IMAGES
overq = pygame.image.load("fundo_overq_intro.png")
overq_rect = overq.get_rect()
overq = pygame.transform.scale(overq, (1000, 600))
overq_rect.topleft = (0,0)

background = pygame.image.load("fundo.jpg")
background_rect = background.get_rect()
background = pygame.transform.scale(background, (600, 300))
background_rect.topleft = (0,0)

personagem = pygame.image.load("personagem_jogo.png")
personagem = pygame.transform.scale(personagem, (50, 50))
personagem_rect = personagem.get_rect()
personagem_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)



# LOAD TEXT
intro = intro_font.render('IN ASSOCIATION WITH:', True, WHITE)
intro_rect = intro.get_rect()
intro_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

overq_texto= over_q.render('OVER-Q', True, WHITE)
overq_rect = overq_texto.get_rect()
overq_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

mebeo_texto= mebeo.render('MEBEO', True, WHITE)
mebeo_rect = mebeo_texto.get_rect()
mebeo_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

INICIO_text = font_title.render("BUCETA GAME", True, WHITE)
INICIO_rect = INICIO_text.get_rect()
INICIO_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 30)

INICIO_text2 = font.render("APERTE 'ESPACO' PARA COMECAR", True, WHITE)
INICIO_rect2 = INICIO_text2.get_rect()
INICIO_rect2.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 48)



# SET GAME VALUES
velocity = 10


# GAME LOOP
estado = 'INTRO'
running = True 
while running:
    # --------------------------------- INTRO --------------------------------- #
    if estado == 'INTRO':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        contador_intro -= 1
        display_surface.fill(DARK_BLUE)
        display_surface.blit(overq_texto, overq_rect)
        if contador_intro <= 0:
            display_surface.fill(DARK_BLUE)
            display_surface.blit(intro, intro_rect)
            contador_intro_2 -= 1
            if contador_intro_2 <= 0:
                contador_intro_3 -= 1
                display_surface.fill(DARK_BLUE)
                display_surface.blit(mebeo_texto, mebeo_rect)
                if contador_intro_3 <= 0:
                    estado = 'INICIO'
    # --------------------------------- TITLE SCREEN --------------------------------- #
    if estado == 'INICIO':
        display_surface.fill(DARK_BLUE)
        display_surface.blit(INICIO_text, INICIO_rect)
        display_surface.blit(INICIO_text2, INICIO_rect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                estado = 'JOGANDO'

    if estado == 'JOGANDO':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.fill(DARK_BLUE)


        keys = pygame.key.get_pressed()

        # MOVE DRAGON

        if keys[pygame.K_a] and personagem_rect.left > 0:
            personagem_rect.x -= velocity
        if keys[pygame.K_d] and personagem_rect.right < WINDOW_WIDTH:
            personagem_rect.x += velocity
        if keys[pygame.K_w] and personagem_rect.top > 0:
            personagem_rect.y -= velocity
        if keys[pygame.K_s] and personagem_rect.bottom < WINDOW_HEIGHT:
            personagem_rect.y += velocity

        display_surface.blit(personagem, personagem_rect)
        pygame.draw.rect(display_surface, (255, 0, 0), personagem_rect, 2)
        pygame.display.update()


        # FIM DE JOGO
    pygame.display.update()
    clock.tick(FPS)


# END OF THE GAME
pygame.quit()