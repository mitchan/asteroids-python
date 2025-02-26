import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        updatable.update(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
