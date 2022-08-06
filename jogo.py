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
BLUE = (0, 0, 255)
ORANGE = (255, 100, 10)
# FONTS
intro_font = pygame.font.Font("assets/galaxia.otf", 70)
font = pygame.font.Font("assets/galaxia.otf", 37)
font_title = pygame.font.Font("assets/galaxia.otf", 150)
over_q = pygame.font.Font("assets/overq_font.ttf", 100)
mebeo = pygame.font.Font("assets/mebeo_true.ttf", 100)


# CREATE A DISPLAY SURFACE AND SET ITS CAPTIONS
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('OVER-Q')

# LOAD IMAGES
overq = pygame.image.load("assets/fundo_overq_intro.png")
overq_rect = overq.get_rect()
overq = pygame.transform.scale(overq, (1000, 600))
overq_rect.topleft = (0,0)

background = pygame.image.load("assets/fundo.jpg")
background_rect = background.get_rect()
background = pygame.transform.scale(background, (600, 300))
background_rect.topleft = (0,0)

#CORACAO AZUL
coracaoazul = pygame.image.load("assets/coracaoazul.png")
coracaoazul_rect = coracaoazul.get_rect()
coracaoazul = pygame.transform.scale(coracaoazul, (50, 50))
coracaoazul_rect.topleft = (WINDOW_WIDTH-50,5)

coracaoazul2 = pygame.image.load("assets/coracaoazul.png")
coracaoazul_rect2 = coracaoazul2.get_rect()
coracaoazul2 = pygame.transform.scale(coracaoazul2, (50, 50))
coracaoazul_rect2.topleft = (WINDOW_WIDTH-110,5)

coracaoazul3 = pygame.image.load("assets/coracaoazul.png")
coracaoazul_rect3 = coracaoazul3.get_rect()
coracaoazul3 = pygame.transform.scale(coracaoazul3, (50, 50))
coracaoazul_rect3.topleft = (WINDOW_WIDTH-170,5)


#CORACAO AZUL DPS Q DA DANO :(
coracao_azul_dano = pygame.image.load("assets/coracaoazuldano.png")
coracao_azul_dano_rect = coracao_azul_dano.get_rect()
coracao_azul_dano = pygame.transform.scale(coracao_azul_dano, (50, 50))
coracao_azul_dano_rect.topleft = (WINDOW_WIDTH-50,5)

coracao_azul_dano2 = pygame.image.load("assets/coracaoazuldano.png")
coracao_azul_dano_rect2 = coracao_azul_dano2.get_rect()
coracao_azul_dano2 = pygame.transform.scale(coracao_azul_dano2, (50, 50))
coracao_azul_dano_rect2.topleft = (WINDOW_WIDTH-110,5)


coracao_azul_dano3 = pygame.image.load("assets/coracaoazuldano.png")
coracao_azul_dano_rect3 = coracao_azul_dano3.get_rect()
coracao_azul_dano3 = pygame.transform.scale(coracao_azul_dano3, (50, 50))
coracao_azul_dano_rect3.topleft = (WINDOW_WIDTH-170,5)


#CORACAO LARANJA

coracaolaranja = pygame.image.load("assets/coracaolaranja.png")
coracaolaranja_rect = coracaolaranja.get_rect()
coracaolaranja = pygame.transform.scale(coracaolaranja, (50, 50))
coracaolaranja_rect.topleft = (0,5)

coracaolaranja2 = pygame.image.load("assets/coracaolaranja.png")
coracaolaranja_rect2 = coracaolaranja2.get_rect()
coracaolaranja2 = pygame.transform.scale(coracaolaranja2, (50, 50))
coracaolaranja_rect2.topleft = (60,5)

coracaolaranja3 = pygame.image.load("assets/coracaolaranja.png")
coracaolaranja_rect3 = coracaolaranja3.get_rect()
coracaolaranja3 = pygame.transform.scale(coracaolaranja3, (50, 50))
coracaolaranja_rect3.topleft = (120,5)

#PERSONAGEM 1
personagem = pygame.image.load("assets/personagem_jogo.png")
personagem = pygame.transform.scale(personagem, (50, 50))
personagem_rect = personagem.get_rect()
personagem_rect.center = (120, WINDOW_HEIGHT-26)

#PERSONAGEM 2
personagem2 = pygame.image.load("assets/personagem2.png")
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

vida1 = 30
vida2 = 30

p1_r_bullet = False
p1_l_bullet = False
p2_r_bullet = False
p2_l_bullet = False

p1_bullets = []
p1_bullets_l = []
p1_bullets_r = []
p2_bullets = []
p2_bullets_l = []
p2_bullets_r = []
bullet_vel = 7
max_bullets = 3

P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2


def handle_bullets_right(p1_bullets_r, p2_bullets_r, personagem, personagem2):
    for bullet in p1_bullets_r:
        bullet.x += bullet_vel
        if personagem2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet)
            p1_bullets_r.remove(bullet)

        elif bullet.x > WINDOW_WIDTH or bullet.x<0:
            p1_bullets.remove(bullet)
            p1_bullets_r.remove(bullet)

    for bullet in p2_bullets_r:
        bullet.x += bullet_vel     
        if personagem.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p2_bullets.remove(bullet)
            p2_bullets_r.remove(bullet)
        elif bullet.x < 0 or bullet.x>WINDOW_WIDTH:
            p2_bullets.remove(bullet)
            p2_bullets_r.remove(bullet)

def handle_bullets_left(p1_bullets_l, p2_bullets_l, personagem, personagem2):
    for bullet in p1_bullets_l:
        bullet.x -= bullet_vel
        if personagem2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet)
            p1_bullets_l.remove(bullet)
            
        elif bullet.x > WINDOW_WIDTH or bullet.x<0:
            p1_bullets.remove(bullet)
            p1_bullets_l.remove(bullet)
    for bullet in p2_bullets_l:
        bullet.x -= bullet_vel     
        if personagem.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p2_bullets.remove(bullet)
            p2_bullets_l.remove(bullet)
        elif bullet.x < 0 or bullet.x>WINDOW_WIDTH:
            p2_bullets.remove(bullet)
            p2_bullets_l.remove(bullet)


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and len(p1_bullets) < max_bullets:
                    bullet = pygame.Rect(personagem_rect.x, personagem_rect.y + personagem_rect.height//2, 10, 5)
                    p1_bullets.append(bullet)
                    p1_bullets_l.append(bullet)
                if event.key == pygame.K_e and len(p1_bullets) < max_bullets:
                    bullet = pygame.Rect(personagem_rect.x + personagem_rect.width, personagem_rect.y + personagem_rect.height//2, 10, 5)
                    p1_bullets.append(bullet)
                    p1_bullets_r.append(bullet)
                if event.key == pygame.K_u and len(p2_bullets) < max_bullets:
                    bullet = pygame.Rect(personagem_rect2.x, personagem_rect2.y + personagem_rect2.height//2, 10, 5)
                    p2_bullets.append(bullet)
                    p2_bullets_l.append(bullet)
                if event.key == pygame.K_o and len(p2_bullets) < max_bullets:
                    bullet = pygame.Rect(personagem_rect2.x + personagem_rect2.width, personagem_rect2.y + personagem_rect2.height//2, 10, 5)
                    p2_bullets.append(bullet)
                    p2_bullets_r.append(bullet)


            if event.type == P2_HIT:
                vida2 -= 1
            if event.type == P1_HIT:
                vida1 -= 1
        

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

        #HEARTS
            #AZUL
        
        display_surface.blit(coracaoazul, coracaoazul_rect)
        display_surface.blit(coracaoazul2, coracaoazul_rect2)
        display_surface.blit(coracaoazul3, coracaoazul_rect3)
            #LARANJA
        display_surface.blit(coracaolaranja, coracaolaranja_rect)
        display_surface.blit(coracaolaranja2, coracaolaranja_rect2)
        display_surface.blit(coracaolaranja3, coracaolaranja_rect3)

        #DRAW PLAYER 1
        display_surface.blit(personagem, personagem_rect)
        pygame.draw.rect(display_surface, (255, 0, 0), personagem_rect, 2)
        #DRAW PLAYER 2
        display_surface.blit(personagem2, personagem_rect2)
        pygame.draw.rect(display_surface, (255, 0, 0), personagem_rect2, 2)
        #DRAW BULLETS
        handle_bullets_right(p1_bullets_r, p2_bullets_r, personagem_rect, personagem_rect2)
        handle_bullets_left(p1_bullets_l, p2_bullets_l, personagem_rect, personagem_rect2)
        for bullet in p2_bullets:
            pygame.draw.rect(display_surface, BLUE, bullet)
        for bullet in p1_bullets:
            pygame.draw.rect(display_surface, ORANGE, bullet)
        #DISPLAY UPDATE
        pygame.display.update()

        # FIM DE JOGO
    pygame.display.update()
    clock.tick(FPS)



# END OF THE GAME
pygame.quit()