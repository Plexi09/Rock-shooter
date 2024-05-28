import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
delta_time = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys [pygame.K_z]:
        player_pos.y -= 300 * delta_time
    if keys [pygame.K_s]:
        player_pos.y += 300 * delta_time
    if keys [pygame.K_q]:
        player_pos.x -= 300 * delta_time
    if keys [pygame.K_d]:
        player_pos.x += 300 * delta_time
    if keys [pygame.K_ESCAPE]:
        running = False


    pygame.display.flip()
    delta_time = clock.tick(60) / 1000

pygame.quit()