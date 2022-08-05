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
intro_font = pygame.font.Font("game/galaxia.otf", 70)
font = pygame.font.Font("game/galaxia.otf", 37)
font_title = pygame.font.Font("game/galaxia.otf", 150)
over_q = pygame.font.Font("game/overq_font.ttf", 100)
mebeo = pygame.font.Font("game/mebeo_true.ttf", 100)


# CREATE A DISPLAY SURVACE AND SET ITS CAPTIONS
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('OVER-Q')

# LOAD IMAGES
overq = pygame.image.load("game/fundo_overq_intro.png")
overq_rect = overq.get_rect()
overq = pygame.transform.scale(overq, (1000, 600))
overq_rect.topleft = (0,0)

background = pygame.image.load("game/fundo.jpg")
background_rect = background.get_rect()
background = pygame.transform.scale(background, (600, 300))
background_rect.topleft = (0,0)

#PERSONAGEM 1
personagem = pygame.image.load("game/personagem_jogo.png")
personagem = pygame.transform.scale(personagem, (50, 50))
personagem_rect = personagem.get_rect()
personagem_rect.center = (120, WINDOW_HEIGHT-26)

#PERSONAGEM 2
personagem2 = pygame.image.load("game/personagem2.png")
personagem2 = pygame.transform.scale(personagem2, (50, 50))
personagem_rect2 = personagem2.get_rect()
personagem_rect2.center = (WINDOW_WIDTH-120, WINDOW_HEIGHT-26)


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
velocity_x1 = 10
velocity_x2 = 10
velocity_y1 = 20
velocity_y2 = 20

jump1 = False
jump2 = False

dash1 = False
dash2 = False
tempo_dash1 = 20
tempo_dash2 = 20

vida1 = 10
vida2 = 10


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
    



        # MOVE PLAYER 1
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and personagem_rect.left > 0:
            personagem_rect.x -= velocity_x1
        if keys[pygame.K_d] and personagem_rect.right < WINDOW_WIDTH:
            personagem_rect.x += velocity_x1
        if jump1 == False and keys[pygame.K_w]:
            jump1 = True
        if jump1:
            personagem_rect.y -= velocity_y1
            velocity_y1 -= 1
            if velocity_y1 <- 20:
                jump1 = False
                velocity_y1 = 20
        if dash1 == False and keys[pygame.K_s]:
            dash1 = True
            tempo_dash1 = 20
        if dash1:
            tempo_dash1 -= 5
            velocity_x1 += 10
            if tempo_dash1 <= 0:
                velocity_x1 = 10
                dash1 = False
            


        # MOVE PLAYER 2
        if keys[pygame.K_j] and personagem_rect2.left > 0:
            personagem_rect2.x -= velocity_x2
        if keys[pygame.K_l] and personagem_rect2.right < WINDOW_WIDTH:
            personagem_rect2.x += velocity_x2
        if jump2 == False and keys[pygame.K_i]:
            jump2 = True
        if jump2:
            personagem_rect2.y -= velocity_y2
            velocity_y2 -= 1
            if velocity_y2 <- 20:
                jump2 = False
                velocity_y2 = 20
        if dash2 == False and keys[pygame.K_k]:
            dash2 = True
            tempo_dash2 = 20
        if dash2:
            tempo_dash2 -= 5
            velocity_x2 += 10
            if tempo_dash2 <= 0:
                velocity_x2 = 10
                dash2 = False  

        
        #DRAW PLAYER 1
        display_surface.blit(personagem, personagem_rect)
        pygame.draw.rect(display_surface, (255, 0, 0), personagem_rect, 2)
        #DRAW PLAYER 2
        display_surface.blit(personagem2, personagem_rect2)
        pygame.draw.rect(display_surface, (255, 0, 0), personagem_rect2, 2)
        #DISPLAY UPDATE
        pygame.display.update()

        # FIM DE JOGO
    pygame.display.update()
    clock.tick(FPS)



# END OF THE GAME
pygame.quit()