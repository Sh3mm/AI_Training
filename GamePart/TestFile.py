import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("race game")

PS = [50, 50, 50, 50]
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        PS[0] -= vel

    if keys[pygame.K_RIGHT]:
        PS[0] += vel

    if keys[pygame.K_UP]:
        PS[1] -= vel

    if keys[pygame.K_DOWN]:
        PS[1] += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 0), PS)
    pygame.display.update()

pygame.quit()
