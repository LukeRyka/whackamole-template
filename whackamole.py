import pygame
import random

GRID_SIZE = (20,16)
SQUARE_SIZE = 32
TOTAL_SIZE = (GRID_SIZE[0] * SQUARE_SIZE, GRID_SIZE[1] * SQUARE_SIZE)

def draw_grid(screen):
    for x in range(0, TOTAL_SIZE[0], SQUARE_SIZE):
        pygame.draw.line(screen, "black", (x,0), (x,TOTAL_SIZE[1]))
    for y in range(0, TOTAL_SIZE[1], SQUARE_SIZE):
        pygame.draw.line(screen, "black", (0,y), (TOTAL_SIZE[0], y))

def get_random_position():
    col = random.randrange(0, GRID_SIZE[0])
    row = random.randrange(0,GRID_SIZE[1])
    return col * SQUARE_SIZE, row * SQUARE_SIZE

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_position = (0,0)
        screen = pygame.display.set_mode((640, 512)) #these values correspond with TOTAL_SIZE
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_x, mole_y = mole_position
                    if mole_x <= mouse_x < mole_x + SQUARE_SIZE and mole_y <= mouse_y < mole_y + SQUARE_SIZE:
                        mole_position = get_random_position()
            screen.fill("light green")
            draw_grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
