import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Prueba Pygame")
font = pygame.font.SysFont("arial", 28)
clock = pygame.time.Clock()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 45))
    text = font.render("¡Pygame está funcionando! (cierra la ventana)", True, (230, 230, 240))
    screen.blit(text, (40, 180))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()