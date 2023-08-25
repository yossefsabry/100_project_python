import pygame

# first make the window and define the varibles =>
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_CAPTION = pygame.display.set_caption("hello from yossef")
# ITEM define the varibles =>
WIDTH_ITEM = 40
HEIGHT_ITEM = 40
ITEM_X = 400 - (WIDTH_ITEM / 2)
ITEM_Y = 450 - (HEIGHT_ITEM / 2)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
STEP = 20

# speed for item
speed = 10
is_jumping = False

while True:
    pygame.time.delay(100)

    SCREEN.fill(WHITE)
    # first make the item for the gamex
    pygame.draw.rect(SCREEN, RED, (ITEM_X, ITEM_Y, WIDTH_ITEM, HEIGHT_ITEM))

    # to store the keys user input
    keys = pygame.key.get_pressed()

    # for exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if keys[pygame.K_LEFT] and ITEM_X > 0:
        ITEM_X -= STEP  # <==> ITEM_X = ITEM_X - STEP
    if keys[pygame.K_RIGHT] and ITEM_X < SCREEN_WIDTH - WIDTH_ITEM:
        ITEM_X += STEP  # <==> ITEM_X = ITEM_X - STEP
    if not is_jumping:  # <==> if is_jumping == False:
        if keys[pygame.K_UP] and ITEM_Y > 0:
            ITEM_Y -= STEP  # <==> ITEM_X = ITEM_X - STEP
        if keys[pygame.K_DOWN] and ITEM_Y < SCREEN_HEIGHT - HEIGHT_ITEM:
            ITEM_Y += STEP  # <==> ITEM_X = ITEM_X - STEP
        if keys[pygame.K_SPACE]:
            is_jumping = True
    if is_jumping:  # <==> if is_jumping == True:
        if speed >= -10:
            # sign for change the directory for the jump
            sign = 1
            if speed < 0:
                sign = -1
            ITEM_Y -= speed ** 2 / 1.4 * sign
            speed -= 1
        else:
            speed = 10
            is_jumping = False

    pygame.display.update()
